import base64
from collections import deque
from colorsys import hsv_to_rgb
from datetime import datetime
import json
from pathlib import Path
import random
import socket
import threading
import time

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import requests
import uvicorn


BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"
CONFIG_PATH = BASE_DIR / "config.json"


DEFAULT_CONFIG = {
    "web_host": "0.0.0.0",
    "web_port": 5000,
    "rest_api_url": "http://127.0.0.1:8212/v1/api",
    "rest_user": "admin",
    "rest_password": "CHANGE_ME",
    "poll_interval_seconds": 3,
    "history_limit": 15,
    "map_image_size": 8192,
    "map_background": "#0b1520",
    "world_bounds": {
        "min_x": -2121.79,
        "max_x": 1200.06,
        "min_y": -2167.88,
        "max_y": 1762.90,
    },
    "map_layers": [
        {
            "id": "world_map",
            "image_url": "/static/T_WorldMap.png",
            "image_width": 8192,
            "image_height": 8192,
            "image_to_world": {
                "a": 0.375711236,
                "b": -0.0156508073,
                "c": -1823.80271,
                "d": -0.00463658188,
                "e": -0.385279301,
                "f": 1056.84169,
            },
        },
        {
            "id": "tree_map",
            "image_url": "/static/T_TreeMap.png",
            "image_width": 8192,
            "image_height": 8192,
            "image_to_world": {
                "a": 0.0862548982233,
                "b": 0.00221230612851,
                "c": -2123.21210,
                "d": -0.0005399869936045,
                "e": -0.08862828935115,
                "f": 1769.06075,
            },
        },
    ],
    "coordinate_transform": {
        "offset_for_location_y": -157664.55791065,
        "offset_for_location_x": 123467.1611767,
        "scale": 462.962962963,
        "post_correction": {
            "x_from_x": 1.00839296,
            "x_from_y": -0.000291515566,
            "x_offset": -0.723745275,
            "y_from_x": -0.000516414825,
            "y_from_y": 1.00833931,
            "y_offset": 0.172689105,
        },
    },
    "color_settings": {
        "minimum_lightness": 0.56,
        "minimum_distance": 115.0,
        "saturation_min": 0.62,
        "saturation_max": 0.9,
    },
    "ui_settings": {
        "default_language": "en",
    },
}


def deep_merge(base, override):
    result = dict(base)
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(result.get(key), dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result


def load_config():
    if not CONFIG_PATH.exists():
        CONFIG_PATH.write_text(
            json.dumps(DEFAULT_CONFIG, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
        return dict(DEFAULT_CONFIG)

    loaded = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    return deep_merge(DEFAULT_CONFIG, loaded)


def save_config(config):
    CONFIG_PATH.write_text(
        json.dumps(config, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


class LogBuffer:
    def __init__(self, maxlen=400):
        self.items = deque(maxlen=maxlen)
        self.lock = threading.Lock()

    def add(self, level, message):
        entry = {
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "level": level,
            "message": str(message),
        }
        with self.lock:
            self.items.append(entry)
        print(f"[{entry['time']}] [{level}] {message}")

    def snapshot(self):
        with self.lock:
            return list(self.items)


CONFIG = load_config()
LOGS = LogBuffer()


def coerce_float(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def rgb_distance(color_a, color_b):
    return sum((a - b) ** 2 for a, b in zip(color_a, color_b)) ** 0.5


def relative_lightness(rgb):
    red, green, blue = [channel / 255 for channel in rgb]
    return (max(red, green, blue) + min(red, green, blue)) / 2


def rgb_to_hex(rgb):
    return "#{:02X}{:02X}{:02X}".format(*rgb)


def hex_to_rgb(color):
    cleaned = color.lstrip("#")
    return tuple(int(cleaned[index:index + 2], 16) for index in (0, 2, 4))


class ColorPool:
    def __init__(self, settings):
        self.apply_settings(settings)

    def apply_settings(self, settings):
        self.minimum_lightness = float(settings["minimum_lightness"])
        self.minimum_distance = float(settings["minimum_distance"])
        self.saturation_min = float(settings["saturation_min"])
        self.saturation_max = float(settings["saturation_max"])

    def generate(self, used_colors):
        used_rgb = [hex_to_rgb(color) for color in used_colors]
        best_candidate = None
        best_score = -1.0

        for _ in range(768):
            hue = random.random()
            saturation = random.uniform(self.saturation_min, self.saturation_max)
            value = random.uniform(0.84, 1.0)
            rgb = tuple(int(channel * 255) for channel in hsv_to_rgb(hue, saturation, value))

            if relative_lightness(rgb) < self.minimum_lightness:
                continue

            if not used_rgb:
                return rgb_to_hex(rgb)

            score = min(rgb_distance(rgb, existing) for existing in used_rgb)
            if score >= self.minimum_distance:
                return rgb_to_hex(rgb)

            if score > best_score:
                best_candidate = rgb
                best_score = score

        if best_candidate is not None:
            return rgb_to_hex(best_candidate)

        fallback = tuple(int(channel * 255) for channel in hsv_to_rgb(random.random(), 0.8, 0.96))
        return rgb_to_hex(fallback)


class PlayerManager:
    def __init__(self, config):
        self.players = {}
        self.assigned_colors = {}
        self.connection_events = deque(maxlen=400)
        self.last_poll_at = None
        self.last_error = None
        self.lock = threading.Lock()
        self.configure(config)

    def configure(self, config):
        self.history_limit = int(config["history_limit"])
        self.poll_interval_seconds = int(config["poll_interval_seconds"])
        self.map_image_size = int(config["map_image_size"])
        self.map_background = str(config["map_background"])
        self.map_layers = [dict(layer) for layer in config["map_layers"]]
        self.world_bounds = self.calculate_world_bounds(self.map_layers, config["world_bounds"])
        transform = config["coordinate_transform"]
        self.offset_for_location_y = float(transform["offset_for_location_y"])
        self.offset_for_location_x = float(transform["offset_for_location_x"])
        self.scale = float(transform["scale"])
        post_correction = transform.get("post_correction", {})
        self.post_x_from_x = float(post_correction.get("x_from_x", 1.0))
        self.post_x_from_y = float(post_correction.get("x_from_y", 0.0))
        self.post_x_offset = float(post_correction.get("x_offset", 0.0))
        self.post_y_from_x = float(post_correction.get("y_from_x", 0.0))
        self.post_y_from_y = float(post_correction.get("y_from_y", 1.0))
        self.post_y_offset = float(post_correction.get("y_offset", 0.0))
        if hasattr(self, "color_pool"):
            self.color_pool.apply_settings(config["color_settings"])
        else:
            self.color_pool = ColorPool(config["color_settings"])
        with self.lock:
            for player in self.players.values():
                player["history"] = deque(player["history"], maxlen=self.history_limit)

    @staticmethod
    def calculate_world_bounds(map_layers, fallback_bounds):
        xs = []
        ys = []

        for layer in map_layers:
            transform = layer["image_to_world"]
            width = float(layer["image_width"])
            height = float(layer["image_height"])
            corners = [
                (0.0, 0.0),
                (width, 0.0),
                (0.0, height),
                (width, height),
            ]

            for image_x, image_y in corners:
                world_x = (
                    transform["a"] * image_x
                    + transform["b"] * image_y
                    + transform["c"]
                )
                world_y = (
                    transform["d"] * image_x
                    + transform["e"] * image_y
                    + transform["f"]
                )
                xs.append(world_x)
                ys.append(world_y)

        if not xs or not ys:
            return dict(fallback_bounds)

        return {
            "min_x": min(xs),
            "max_x": max(xs),
            "min_y": min(ys),
            "max_y": max(ys),
        }

    def rest_headers(self):
        auth = base64.b64encode(
            f"{CONFIG['rest_user']}:{CONFIG['rest_password']}".encode("ascii")
        ).decode("ascii")
        return {"Authorization": f"Basic {auth}"}

    def rest_request(self, method, path, **kwargs):
        headers = kwargs.pop("headers", {})
        headers = {**self.rest_headers(), **headers}
        return requests.request(
            method,
            f"{CONFIG['rest_api_url']}{path}",
            headers=headers,
            **kwargs,
        )

    def sav_to_map(self, raw_x, raw_y):
        base_x = (raw_y + self.offset_for_location_y) / self.scale
        base_y = (raw_x + self.offset_for_location_x) / self.scale
        return {
            "x": (
                (base_x * self.post_x_from_x)
                + (base_y * self.post_x_from_y)
                + self.post_x_offset
            ),
            "y": (
                (base_x * self.post_y_from_x)
                + (base_y * self.post_y_from_y)
                + self.post_y_offset
            ),
        }

    def normalize_position(self, raw_x, raw_y):
        if -2000 <= raw_x <= 2000 and -2000 <= raw_y <= 2000:
            return {
                "raw": {"x": raw_x, "y": raw_y},
                "map": {"x": raw_x, "y": raw_y},
                "source": "map",
            }

        return {
            "raw": {"x": raw_x, "y": raw_y},
            "map": self.sav_to_map(raw_x, raw_y),
            "source": "sav",
        }

    def assign_color(self, steam_id):
        color = self.color_pool.generate(self.assigned_colors.values())
        self.assigned_colors[steam_id] = color
        return color

    def clear_players(self):
        with self.lock:
            self.players.clear()
            self.assigned_colors.clear()
            self.connection_events.clear()
            self.last_poll_at = datetime.now().isoformat(timespec="seconds")

    def set_error(self, message):
        with self.lock:
            self.last_error = message

    def sync_players(self, payload_players):
        active_ids = set()
        polled_at = datetime.now().isoformat(timespec="seconds")

        with self.lock:
            for item in payload_players:
                steam_id = str(
                    item.get("userId")
                    or item.get("playerId")
                    or item.get("accountName")
                    or item.get("name")
                    or ""
                ).strip()
                if not steam_id:
                    continue

                raw_x = coerce_float(item.get("location_x"))
                raw_y = coerce_float(item.get("location_y"))
                if raw_x is None or raw_y is None:
                    continue

                normalized = self.normalize_position(raw_x, raw_y)
                map_position = normalized["map"]
                active_ids.add(steam_id)

                player = self.players.get(steam_id)
                if player is None:
                    player = {
                        "steamid": steam_id,
                        "name": str(item.get("name") or item.get("accountName") or "Unknown"),
                        "level": int(item.get("level") or 0),
                        "position": map_position,
                        "history": deque(maxlen=self.history_limit),
                        "color": self.assign_color(steam_id),
                        "last_update": polled_at,
                        "raw_position": normalized["raw"],
                        "coordinate_source": normalized["source"],
                    }
                    self.players[steam_id] = player
                    self.connection_events.appendleft(
                        {
                            "time": polled_at,
                            "type": "join",
                            "steamid": steam_id,
                            "name": player["name"],
                            "level": player["level"],
                        }
                    )

                player["name"] = str(item.get("name") or item.get("accountName") or player["name"])
                player["level"] = int(item.get("level") or 0)
                player["position"] = map_position
                player["raw_position"] = normalized["raw"]
                player["coordinate_source"] = normalized["source"]
                player["last_update"] = polled_at

                if (
                    not player["history"]
                    or abs(player["history"][-1]["x"] - map_position["x"]) > 0.01
                    or abs(player["history"][-1]["y"] - map_position["y"]) > 0.01
                ):
                    player["history"].append({"x": map_position["x"], "y": map_position["y"]})

            offline_ids = [steam_id for steam_id in list(self.players.keys()) if steam_id not in active_ids]
            for steam_id in offline_ids:
                offline_player = self.players[steam_id]
                self.connection_events.appendleft(
                    {
                        "time": polled_at,
                        "type": "leave",
                        "steamid": steam_id,
                        "name": offline_player["name"],
                        "level": offline_player["level"],
                    }
                )
                self.assigned_colors.pop(steam_id, None)
                del self.players[steam_id]

            self.last_poll_at = polled_at
            self.last_error = None

    def snapshot(self):
        with self.lock:
            players = [
                {
                    "steamid": player["steamid"],
                    "name": player["name"],
                    "level": player["level"],
                    "position": dict(player["position"]),
                    "raw_position": dict(player["raw_position"]),
                    "coordinate_source": player["coordinate_source"],
                    "history": list(player["history"]),
                    "color": player["color"],
                    "last_update": player["last_update"],
                }
                for player in self.players.values()
            ]
            players.sort(key=lambda item: item["name"].lower())

            return {
                "players": players,
                "connection_events": list(self.connection_events),
                "updated_at": self.last_poll_at,
                "error": self.last_error,
            }


player_manager = PlayerManager(CONFIG)
app = FastAPI()
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")


def get_local_ip():
    probe = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        probe.connect(("8.8.8.8", 80))
        return probe.getsockname()[0]
    except Exception:
        return "127.0.0.1"
    finally:
        probe.close()


def get_external_ip():
    try:
        response = requests.get("https://api.ipify.org?format=json", timeout=4)
        response.raise_for_status()
        return response.json().get("ip")
    except Exception:
        return None


def ensure_local_request(request: Request):
    client_host = (request.client.host if request.client else "") or ""
    if client_host not in {"127.0.0.1", "::1"}:
        raise HTTPException(status_code=403, detail="Admin access is limited to localhost.")


@app.get("/")
async def index():
    return FileResponse(STATIC_DIR / "index.html")


@app.get("/admin")
async def admin(request: Request):
    ensure_local_request(request)
    return FileResponse(STATIC_DIR / "admin.html")


@app.get("/api/players")
async def api_players():
    snapshot = player_manager.snapshot()
    return JSONResponse(
        {
            "players": snapshot["players"],
            "count": len(snapshot["players"]),
            "updated_at": snapshot["updated_at"],
            "error": snapshot["error"],
            "poll_interval": player_manager.poll_interval_seconds,
            "server_running": True,
            "connection_events": snapshot["connection_events"][:120],
            "map": {
                "background": player_manager.map_background,
                "world_bounds": player_manager.world_bounds,
                "layers": player_manager.map_layers,
                "coordinate_transform": {
                    "source": "palserver-online-map calibrated",
                    "offset_for_location_y": player_manager.offset_for_location_y,
                    "offset_for_location_x": player_manager.offset_for_location_x,
                    "scale": player_manager.scale,
                    "axis_swap": True,
                    "post_correction": {
                        "x_from_x": player_manager.post_x_from_x,
                        "x_from_y": player_manager.post_x_from_y,
                        "x_offset": player_manager.post_x_offset,
                        "y_from_x": player_manager.post_y_from_x,
                        "y_from_y": player_manager.post_y_from_y,
                        "y_offset": player_manager.post_y_offset,
                    },
                },
            },
        }
    )


@app.get("/api/status")
async def api_status(request: Request):
    ensure_local_request(request)
    snapshot = player_manager.snapshot()
    external_ip = get_external_ip()
    external_link = f"http://{external_ip}:{CONFIG['web_port']}" if external_ip else None
    return JSONResponse(
        {
            "config": CONFIG,
            "player_count": len(snapshot["players"]),
            "updated_at": snapshot["updated_at"],
            "last_error": snapshot["error"],
            "links": {
                "external": external_link,
            },
            "logs": LOGS.snapshot()[-50:],
            "players": snapshot["players"],
            "connection_events": snapshot["connection_events"][:120],
        }
    )


@app.get("/api/config")
async def api_get_config(request: Request):
    ensure_local_request(request)
    return JSONResponse(CONFIG)


@app.post("/api/config")
async def api_save_config(payload: dict, request: Request):
    ensure_local_request(request)
    required_numbers = {
        "poll_interval_seconds": 1,
        "history_limit": 1,
        "web_port": 1,
        "map_image_size": 256,
    }
    new_config = deep_merge(CONFIG, payload)

    for key, minimum in required_numbers.items():
        if int(new_config[key]) < minimum:
            raise HTTPException(status_code=400, detail=f"{key} must be >= {minimum}")

    CONFIG.clear()
    CONFIG.update(new_config)
    save_config(CONFIG)
    player_manager.configure(CONFIG)
    LOGS.add("INFO", "Configuration updated from admin UI.")
    return JSONResponse({"ok": True, "config": CONFIG})


def poll_players_loop():
    while True:
        try:
            response = player_manager.rest_request("GET", "/players", timeout=5)
            response.raise_for_status()
            payload = response.json()

            if isinstance(payload, dict):
                payload_players = payload.get("players", [])
            elif isinstance(payload, list):
                payload_players = payload
            else:
                payload_players = []

            if not isinstance(payload_players, list):
                payload_players = []

            player_manager.sync_players(payload_players)
            LOGS.add(
                "INFO",
                f"Player poll OK : {len(payload_players)} players",
            )
        except Exception as exc:
            player_manager.set_error(str(exc))
            LOGS.add("ERROR", f"Player poll failed : {exc}")

        time.sleep(player_manager.poll_interval_seconds)


def main():
    LOGS.add("INFO", "Palworld Live Map Portable starting.")
    LOGS.add("INFO", f"Admin UI: http://127.0.0.1:{CONFIG['web_port']}/admin")
    LOGS.add("INFO", f"Live Map: http://127.0.0.1:{CONFIG['web_port']}")
    threading.Thread(target=poll_players_loop, daemon=True).start()
    uvicorn.run(
        app,
        host=CONFIG["web_host"],
        port=int(CONFIG["web_port"]),
        log_level="warning",
    )


if __name__ == "__main__":
    main()
