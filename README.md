# Palworld Live Map Portable

Made by 4zr  
[https://github.com/crazykorea](https://github.com/crazykorea)  
CC0 1.0 Universal applies only to the original source code and original project assets created by 4zr.

This project is an unofficial fan-made tool and is not affiliated with or endorsed by Pocketpair.

---

## English

### Before You Download

- This package already includes a portable Python runtime.
- You do not need to install Python separately.
- Download the repository as a ZIP from GitHub, or clone it with GitHub Desktop.

### License Scope

- CC0 applies only to the original source code and original project assets created by 4zr.
- Palworld-related names, maps, images, and other game-derived assets are excluded from the CC0 dedication.
- The bundled portable Python runtime and other third-party components are also excluded from the CC0 dedication.
- See `COPYRIGHT-CC0.txt` and `THIRD_PARTY_NOTICES.txt` for details.

### Server Preparation

1. Open `PalWorldSettings.ini`.
2. Set `RESTAPIEnabled=True`.
3. Set `AdminPassword=YOUR_PASSWORD`.

### How To Run

1. Download this repository from GitHub.
2. Extract the ZIP to a normal folder.
3. Open the extracted folder.
4. Run `start.bat`.
5. Wait for your browser to open `http://127.0.0.1:5000/admin`.
6. In Settings, enter the same `AdminPassword` value that you set in `PalWorldSettings.ini`.
7. Click `Apply`.

### Sharing Methods

Direct connection:

- Share `http://PUBLIC_IP:5000`
- Requires router port forwarding for `5000`
- Requires firewall access for `5000`
- Exposes the server's public IP

Cloudflare Tunnel or reverse proxy:

- Share a public URL such as `https://map.example.com`
- Does not require opening port `5000` to the internet
- Helps avoid exposing the origin public IP directly
- The admin page stays local only and must not be exposed through the tunnel or proxy

### Default Settings

- `poll_interval_seconds`: `3`
- `history_limit`: `15`

### Main Notes

- Open the admin page only from `http://127.0.0.1:5000/admin` or `http://localhost:5000/admin`.
- The admin page is blocked through domains, tunnels, and reverse proxies.
- The public Live Map page supports language switching.
- The admin page supports language switching.
- Anyone with the public Live Map link can see player names, map positions, movement trails, and join or leave activity.
- Player join and leave activity is logged automatically.
- `config.example.json` is included in the repository.
- `config.json` is created locally at first run and is not meant to be committed.

### Main Files

- `start.bat`: starts the Live Map
- `app.py`: backend server
- `config.example.json`: example configuration template
- `static/`: web files
- `python/`: bundled portable Python runtime
- `LICENSE`: CC0 license text
- `COPYRIGHT-CC0.txt`: CC0 scope note
- `THIRD_PARTY_NOTICES.txt`: third-party rights and license notice

---

## 한국어

### 다운로드 전 안내

- 이 패키지에는 실행에 필요한 포터블 Python 런타임이 이미 포함되어 있습니다.
- 별도로 Python을 설치할 필요가 없습니다.
- GitHub에서 ZIP으로 다운로드하거나 GitHub Desktop으로 그대로 받아오면 됩니다.

### 라이선스 범위

- CC0는 4zr이 직접 작성한 원본 소스 코드와 직접 제작한 프로젝트 자산에만 적용됩니다.
- Palworld 관련 이름, 지도, 이미지, 기타 게임 기반 자산은 CC0 적용 대상이 아닙니다.
- 포함된 포터블 Python 런타임과 기타 제3자 구성 요소도 CC0 적용 대상이 아닙니다.
- 자세한 내용은 `COPYRIGHT-CC0.txt`, `THIRD_PARTY_NOTICES.txt`를 확인하세요.

### 서버 준비

1. `PalWorldSettings.ini` 파일을 엽니다.
2. `RESTAPIEnabled=True` 로 설정합니다.
3. `AdminPassword=원하는비밀번호` 를 설정합니다.

### 실행 방법

1. GitHub에서 이 저장소를 다운로드합니다.
2. ZIP 파일을 일반 폴더에 압축 해제합니다.
3. 압축 해제한 폴더를 엽니다.
4. `start.bat` 을 실행합니다.
5. 브라우저에서 `http://127.0.0.1:5000/admin` 이 열릴 때까지 기다립니다.
6. 설정에서 `PalWorldSettings.ini` 에 입력한 것과 같은 `AdminPassword` 값을 입력합니다.
7. `적용` 버튼을 누릅니다.

### 공유 방식

직접 연결:

- `http://공인IP:5000` 형식으로 공유합니다.
- 공유기에서 `5000` 포트를 포트 포워딩해야 합니다.
- 방화벽에서 `5000` 포트를 허용해야 합니다.
- 서버의 공인 IP가 그대로 노출됩니다.

Cloudflare Tunnel 또는 리버스 프록시:

- `https://map.example.com` 같은 공개 주소를 공유합니다.
- 외부 인터넷에 `5000` 포트를 직접 열 필요가 없습니다.
- 원본 공인 IP를 직접 노출하지 않는 데 도움이 됩니다.
- 관리자 페이지는 로컬 전용이며, 터널이나 프록시로 외부에 노출하면 안 됩니다.

### 기본 설정값

- `poll_interval_seconds`: `3`
- `history_limit`: `15`

### 주요 안내

- 관리자 페이지는 반드시 `http://127.0.0.1:5000/admin` 또는 `http://localhost:5000/admin` 으로만 여세요.
- 관리자 페이지는 도메인, 터널, 리버스 프록시를 통한 접근이 차단됩니다.
- 공개 Live Map 페이지는 언어 변경을 지원합니다.
- 관리자 페이지도 언어 변경을 지원합니다.
- 공개 Live Map 링크를 받은 사람은 플레이어 이름, 지도 위치, 이동 경로, 접속 및 퇴장 기록을 볼 수 있습니다.
- 플레이어 접속 및 퇴장 기록은 자동으로 저장됩니다.
- 저장소에는 `config.example.json` 이 포함되어 있습니다.
- 실제 `config.json` 은 첫 실행 때 로컬에서 생성되며, 커밋 대상이 아닙니다.

### 주요 파일

- `start.bat`: Live Map 실행
- `app.py`: 백엔드 서버
- `config.example.json`: 예제 설정 템플릿
- `static/`: 웹 파일
- `python/`: 포함된 포터블 Python 런타임
- `LICENSE`: CC0 라이선스 본문
- `COPYRIGHT-CC0.txt`: CC0 적용 범위 안내
- `THIRD_PARTY_NOTICES.txt`: 제3자 권리 및 라이선스 안내

---

## 日本語

### ダウンロード前

- このパッケージには実行に必要なポータブル Python ランタイムがすでに含まれています。
- Python を別途インストールする必要はありません。
- GitHub から ZIP をダウンロードするか、GitHub Desktop でそのまま取得してください。

### ライセンス範囲

- CC0 は 4zr が作成したオリジナルのソースコードとオリジナルのプロジェクト資産にのみ適用されます。
- Palworld 関連の名称、地図、画像、その他のゲーム由来の素材は CC0 の対象外です。
- 同梱されているポータブル Python ランタイムやその他の第三者コンポーネントも CC0 の対象外です。
- 詳細は `COPYRIGHT-CC0.txt` と `THIRD_PARTY_NOTICES.txt` を確認してください。

### サーバー準備

1. `PalWorldSettings.ini` を開きます。
2. `RESTAPIEnabled=True` に設定します。
3. `AdminPassword=任意のパスワード` を設定します。

### 実行方法

1. GitHub からこのリポジトリをダウンロードします。
2. ZIP を通常のフォルダーに展開します。
3. 展開したフォルダーを開きます。
4. `start.bat` を実行します。
5. ブラウザで `http://127.0.0.1:5000/admin` が開くまで待ちます。
6. 設定画面で `PalWorldSettings.ini` に設定したものと同じ `AdminPassword` を入力します。
7. `適用` を押します。

### 共有方法

直接接続:

- `http://PUBLIC_IP:5000` を共有します。
- ルーターで `5000` ポートのポートフォワードが必要です。
- ファイアウォールでも `5000` ポートを許可する必要があります。
- サーバーのグローバル IP がそのまま公開されます。

Cloudflare Tunnel またはリバースプロキシ:

- `https://map.example.com` のような公開 URL を共有します。
- 外部向けに `5000` ポートを直接開放する必要はありません。
- 元のグローバル IP を直接公開しない構成にしやすくなります。
- 管理ページはローカル専用なので、トンネルやプロキシ経由で公開しないでください。

### 既定値

- `poll_interval_seconds`: `3`
- `history_limit`: `15`

### 主な案内

- 管理ページは必ず `http://127.0.0.1:5000/admin` または `http://localhost:5000/admin` から開いてください。
- 管理ページはドメイン、トンネル、リバースプロキシ経由ではブロックされます。
- 公開 Live Map ページは言語切替に対応しています。
- 管理ページも言語切替に対応しています。
- 公開 Live Map のリンクを知っている人は、プレイヤー名、地図上の位置、移動軌跡、参加・退出記録を見ることができます。
- プレイヤーの参加・退出記録は自動的に保存されます。
- リポジトリには `config.example.json` が含まれています。
- 実際の `config.json` は初回起動時にローカルで生成され、コミット対象ではありません。

### 主なファイル

- `start.bat`: Live Map を起動
- `app.py`: バックエンドサーバー
- `config.example.json`: 設定テンプレート
- `static/`: Web ファイル
- `python/`: 同梱ポータブル Python ランタイム
- `LICENSE`: CC0 ライセンス本文
- `COPYRIGHT-CC0.txt`: CC0 適用範囲の案内
- `THIRD_PARTY_NOTICES.txt`: 第三者の権利とライセンス案内

---

## Español

### Antes de descargar

- Este paquete ya incluye un entorno portable de Python.
- No necesitas instalar Python por separado.
- Puedes descargar el repositorio como ZIP desde GitHub o clonarlo con GitHub Desktop.

### Alcance de la licencia

- CC0 se aplica solo al código fuente original y a los recursos originales del proyecto creados por 4zr.
- Los nombres, mapas, imágenes y otros materiales derivados de Palworld quedan excluidos de la dedicación CC0.
- El entorno portable de Python incluido y otros componentes de terceros también quedan excluidos de la dedicación CC0.
- Consulta `COPYRIGHT-CC0.txt` y `THIRD_PARTY_NOTICES.txt` para más detalles.

### Preparación del servidor

1. Abre `PalWorldSettings.ini`.
2. Establece `RESTAPIEnabled=True`.
3. Establece `AdminPassword=TU_CONTRASENA`.

### Cómo ejecutarlo

1. Descarga este repositorio desde GitHub.
2. Extrae el ZIP en una carpeta normal.
3. Abre la carpeta extraída.
4. Ejecuta `start.bat`.
5. Espera a que se abra `http://127.0.0.1:5000/admin` en tu navegador.
6. En Settings, introduce el mismo valor de `AdminPassword` que configuraste en `PalWorldSettings.ini`.
7. Haz clic en `Apply`.

### Métodos para compartir

Conexión directa:

- Comparte `http://IP_PUBLICA:5000`
- Requiere redirección del puerto `5000` en el router
- Requiere permitir el puerto `5000` en el firewall
- Expone la IP pública del servidor

Cloudflare Tunnel o proxy inverso:

- Comparte una URL pública como `https://map.example.com`
- No requiere abrir el puerto `5000` a Internet
- Ayuda a evitar la exposición directa de la IP pública de origen
- La página de administración debe permanecer solo en local y no debe exponerse por el túnel o proxy

### Valores predeterminados

- `poll_interval_seconds`: `3`
- `history_limit`: `15`

### Notas principales

- Abre la página de administración solo desde `http://127.0.0.1:5000/admin` o `http://localhost:5000/admin`.
- La página de administración se bloquea cuando se accede mediante dominios, túneles o proxies inversos.
- La página pública del Live Map permite cambiar el idioma.
- La página de administración también permite cambiar el idioma.
- Cualquier persona que tenga el enlace público del Live Map podrá ver los nombres de los jugadores, sus posiciones en el mapa, sus rutas de movimiento y los registros de entrada y salida.
- El registro de entradas y salidas se guarda automáticamente.
- El repositorio incluye `config.example.json`.
- `config.json` se crea localmente en el primer inicio y no debe subirse al repositorio.

### Archivos principales

- `start.bat`: inicia el Live Map
- `app.py`: servidor backend
- `config.example.json`: plantilla de configuración
- `static/`: archivos web
- `python/`: entorno portable de Python incluido
- `LICENSE`: texto de licencia CC0
- `COPYRIGHT-CC0.txt`: nota sobre el alcance de CC0
- `THIRD_PARTY_NOTICES.txt`: aviso de derechos y licencias de terceros

---

## 中文

### 下载前说明

- 此包已经包含运行所需的便携版 Python 运行环境。
- 无需另外安装 Python。
- 你可以从 GitHub 下载 ZIP，也可以使用 GitHub Desktop 直接克隆。

### 许可范围

- CC0 仅适用于 4zr 创作的原始源代码和原始项目资源。
- Palworld 相关名称、地图、图片以及其他游戏衍生素材不属于 CC0 范围。
- 附带的便携版 Python 运行环境和其他第三方组件也不属于 CC0 范围。
- 详细说明请查看 `COPYRIGHT-CC0.txt` 和 `THIRD_PARTY_NOTICES.txt`。

### 服务器准备

1. 打开 `PalWorldSettings.ini`。
2. 设置 `RESTAPIEnabled=True`。
3. 设置 `AdminPassword=你的密码`。

### 运行方法

1. 从 GitHub 下载此仓库。
2. 将 ZIP 解压到普通文件夹中。
3. 打开解压后的文件夹。
4. 运行 `start.bat`。
5. 等待浏览器打开 `http://127.0.0.1:5000/admin`。
6. 在设置页面中，输入与 `PalWorldSettings.ini` 中相同的 `AdminPassword`。
7. 点击 `应用`。

### 分享方式

直接连接：

- 分享 `http://公网IP:5000`
- 需要在路由器中转发 `5000` 端口
- 需要在防火墙中放行 `5000` 端口
- 会直接暴露服务器的公网 IP

Cloudflare Tunnel 或反向代理：

- 分享类似 `https://map.example.com` 的公开地址
- 不需要把 `5000` 端口直接开放到公网
- 有助于避免直接暴露源站公网 IP
- 管理员页面必须保持本地访问，不能通过隧道或代理对外公开

### 默认设置

- `poll_interval_seconds`: `3`
- `history_limit`: `15`

### 主要说明

- 管理员页面只能通过 `http://127.0.0.1:5000/admin` 或 `http://localhost:5000/admin` 打开。
- 管理员页面会阻止通过域名、隧道和反向代理访问。
- 公开 Live Map 页面支持语言切换。
- 管理员页面也支持语言切换。
- 任何获得公开 Live Map 链接的人，都可以看到玩家名称、地图位置、移动轨迹以及上线和离线记录。
- 玩家上线与离线记录会自动保存。
- 仓库中包含 `config.example.json`。
- 实际 `config.json` 会在首次启动时于本地生成，不应提交到仓库。

### 主要文件

- `start.bat`: 启动 Live Map
- `app.py`: 后端服务器
- `config.example.json`: 配置模板
- `static/`: 网页文件
- `python/`: 附带的便携版 Python 运行环境
- `LICENSE`: CC0 许可正文
- `COPYRIGHT-CC0.txt`: CC0 适用范围说明
- `THIRD_PARTY_NOTICES.txt`: 第三方权利与许可说明
