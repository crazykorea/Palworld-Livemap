# Palworld Live Map Portable

Made by 4zr  
[https://github.com/crazykorea](https://github.com/crazykorea)  
CC0 1.0 Universal

---

## English

### Before You Download

- This package already includes a portable Python runtime.
- You do not need to install Python separately.
- Download the repository as a ZIP from GitHub, or clone it with GitHub Desktop.

### Safe Public Sharing

This program uses the Palworld REST API and exposes a public Live Map address.

If you want to use it on a public server, it is safer to connect a domain that hides the origin public IP through Cloudflare or a similar CDN or reverse proxy service, then share it as `domain:5000`.

### Server Preparation

1. Open `PalWorldSettings.ini`.
2. Set `RESTAPIEnabled=True`.
3. Set `AdminPassword=YOUR_PASSWORD`.
4. Forward port `5000` on your router.
5. Allow port `5000` in Windows Firewall.

### How To Run

1. Download this repository from GitHub.
2. Extract the ZIP to a normal folder.
3. Open the extracted folder.
4. Run `start.bat`.
5. Wait for your browser to open `http://127.0.0.1:5000/admin`.
6. In Settings, make sure `RESTAPIEnabled=True` is set in `PalWorldSettings.ini`, then enter the `AdminPassword` value.
7. Click `Apply`.
8. Share the public Live Map address shown on the admin page with your players.

### Default Settings

- `poll_interval_seconds`: `3`
- `history_limit`: `15`

### Main Notes

- The admin page is limited to the same PC.
- The public Live Map page supports language switching.
- The admin page supports language switching.
- Player join and leave activity is logged automatically.
- You can use a domain such as `your-domain:5000` instead of a raw IP address.

### Main Files

- `start.bat`: starts the Live Map
- `app.py`: backend server
- `config.json`: editable settings
- `static/`: web files
- `python/`: bundled portable Python runtime
- `LICENSE`: CC0 license text
- `COPYRIGHT-CC0.txt`: creator and CC0 dedication note

---

## 한국어

### 다운로드 전에

- 이 패키지에는 실행에 필요한 포터블 Python 런타임이 이미 포함되어 있습니다.
- 별도로 Python을 설치할 필요가 없습니다.
- GitHub에서 ZIP으로 내려받거나, GitHub Desktop으로 그대로 받아도 됩니다.

### 공개 서버 사용 시 권장 방식

이 프로그램은 Palworld REST API를 사용하며, 외부에서 접속 가능한 Live Map 주소를 제공합니다.

공개 서버에서 사용할 경우에는 Cloudflare 등의 CDN 또는 리버스 프록시 서비스를 이용해 원본 공인 IP를 숨긴 도메인을 연결한 뒤, `domain:5000` 형식으로 공유하는 것이 더 안전합니다.

### 서버 준비

1. `PalWorldSettings.ini` 파일을 엽니다.
2. `RESTAPIEnabled=True` 로 설정합니다.
3. `AdminPassword=원하는비밀번호` 를 설정합니다.
4. 공유기에서 `5000` 포트를 포트 포워딩합니다.
5. Windows 방화벽에서 `5000` 포트를 허용합니다.

### 실행 방법

1. GitHub에서 이 저장소를 다운로드합니다.
2. ZIP 파일을 일반 폴더에 압축 해제합니다.
3. 압축 해제한 폴더를 엽니다.
4. `start.bat` 를 실행합니다.
5. 브라우저에서 `http://127.0.0.1:5000/admin` 이 열릴 때까지 기다립니다.
6. 설정에서 `PalWorldSettings.ini` 내부의 `RESTAPIEnabled` 가 `True` 인지 확인하고, `AdminPassword` 값을 입력합니다.
7. `적용` 버튼을 누릅니다.
8. 관리자 페이지에 표시되는 외부 Live Map 주소를 플레이어에게 공유합니다.

### 기본 설정값

- `poll_interval_seconds`: `3`
- `history_limit`: `15`

### 주요 안내

- 관리자 페이지는 같은 PC에서만 열 수 있습니다.
- 공개 Live Map 페이지는 언어 변경을 지원합니다.
- 관리자 페이지도 언어 변경을 지원합니다.
- 플레이어 접속 및 퇴장 기록이 자동으로 저장됩니다.
- 직접 IP 대신 `your-domain:5000` 형식의 도메인 주소를 사용할 수 있습니다.

### 주요 파일

- `start.bat`: Live Map 실행
- `app.py`: 백엔드 서버
- `config.json`: 수정 가능한 설정 파일
- `static/`: 웹 파일
- `python/`: 포함된 포터블 Python 런타임
- `LICENSE`: CC0 라이선스 본문
- `COPYRIGHT-CC0.txt`: 제작자 및 CC0 명시 파일

---

## 日本語

### ダウンロード前

- このパッケージには実行に必要なポータブル Python ランタイムが含まれています。
- Python を別途インストールする必要はありません。
- GitHub から ZIP でダウンロードしても、GitHub Desktop で受け取っても構いません。

### 公開サーバーで使う場合の推奨方法

このプログラムは Palworld REST API を使用し、外部から接続できる Live Map アドレスを提供します。

公開サーバーで使用する場合は、Cloudflare などの CDN またはリバースプロキシサービスを利用して元のグローバル IP を隠したドメインを接続し、`domain:5000` の形式で共有するほうが安全です。

### サーバー準備

1. `PalWorldSettings.ini` を開きます。
2. `RESTAPIEnabled=True` に設定します。
3. `AdminPassword=任意のパスワード` を設定します。
4. ルーターで `5000` ポートをポートフォワーディングします。
5. Windows ファイアウォールで `5000` ポートを許可します。

### 実行方法

1. GitHub からこのリポジトリをダウンロードします。
2. ZIP を通常のフォルダに展開します。
3. 展開したフォルダを開きます。
4. `start.bat` を実行します。
5. ブラウザで `http://127.0.0.1:5000/admin` が開くまで待ちます。
6. 設定で `PalWorldSettings.ini` の `RESTAPIEnabled` が `True` になっていることを確認し、`AdminPassword` の値を入力します。
7. `適用` を押します。
8. 管理ページに表示される公開 Live Map アドレスをプレイヤーへ共有します。

### デフォルト設定

- `poll_interval_seconds`: `3`
- `history_limit`: `15`

### 主な案内

- 管理ページは同じ PC からのみ開けます。
- 公開 Live Map ページは言語切り替えに対応しています。
- 管理ページも言語切り替えに対応しています。
- プレイヤーの参加・退出ログは自動で記録されます。
- 生の IP の代わりに `your-domain:5000` 形式のドメインを使用できます。

### 主なファイル

- `start.bat`: Live Map 起動
- `app.py`: バックエンドサーバー
- `config.json`: 編集可能な設定ファイル
- `static/`: Web ファイル
- `python/`: 同梱ポータブル Python ランタイム
- `LICENSE`: CC0 ライセンス本文
- `COPYRIGHT-CC0.txt`: 制作者および CC0 表記ファイル

---

## Español

### Antes de descargar

- Este paquete ya incluye un entorno portable de Python.
- No necesitas instalar Python por separado.
- Puedes descargar el repositorio como ZIP desde GitHub o recibirlo con GitHub Desktop.

### Uso recomendado en servidores publicos

Este programa usa la REST API de Palworld y ofrece una direccion publica para el Live Map.

Si vas a usarlo en un servidor publico, es mas seguro conectar un dominio que oculte la IP publica de origen mediante Cloudflare u otro servicio CDN o proxy inverso y compartirlo con el formato `domain:5000`.

### Preparacion del servidor

1. Abre `PalWorldSettings.ini`.
2. Establece `RESTAPIEnabled=True`.
3. Establece `AdminPassword=TU_CONTRASENA`.
4. Configura el reenvio del puerto `5000` en tu router.
5. Permite el puerto `5000` en el Firewall de Windows.

### Como ejecutarlo

1. Descarga este repositorio desde GitHub.
2. Extrae el ZIP en una carpeta normal.
3. Abre la carpeta extraida.
4. Ejecuta `start.bat`.
5. Espera a que se abra `http://127.0.0.1:5000/admin` en tu navegador.
6. En Settings, confirma que `RESTAPIEnabled=True` este configurado en `PalWorldSettings.ini` y luego introduce el valor de `AdminPassword`.
7. Haz clic en `Apply`.
8. Comparte con tus jugadores la direccion publica del Live Map que aparece en la pagina de administracion.

### Valores predeterminados

- `poll_interval_seconds`: `3`
- `history_limit`: `15`

### Notas principales

- La pagina de administracion solo puede abrirse desde el mismo PC.
- La pagina publica del Live Map permite cambiar el idioma.
- La pagina de administracion tambien permite cambiar el idioma.
- El registro de entradas y salidas se guarda automaticamente.
- Puedes usar un dominio como `your-domain:5000` en lugar de una IP directa.

### Archivos principales

- `start.bat`: inicia el Live Map
- `app.py`: servidor backend
- `config.json`: configuracion editable
- `static/`: archivos web
- `python/`: entorno portable de Python incluido
- `LICENSE`: texto de licencia CC0
- `COPYRIGHT-CC0.txt`: nota del creador y dedicacion CC0

---

## 中文

### 下载前

- 本包已经包含运行所需的便携版 Python 运行环境。
- 不需要另外安装 Python。
- 你可以从 GitHub 下载 ZIP，也可以用 GitHub Desktop 获取整个仓库。

### 公开服务器的推荐使用方式

本程序使用 Palworld REST API，并提供可从外部访问的 Live Map 地址。

如果要在公开服务器中使用，更安全的做法是通过 Cloudflare 等 CDN 或反向代理服务绑定一个能够隐藏源公网 IP 的域名，并以 `domain:5000` 的形式分享。

### 服务器准备

1. 打开 `PalWorldSettings.ini`。
2. 设置 `RESTAPIEnabled=True`。
3. 设置 `AdminPassword=你的密码`。
4. 在路由器中转发 `5000` 端口。
5. 在 Windows 防火墙中放行 `5000` 端口。

### 运行方法

1. 从 GitHub 下载此仓库。
2. 将 ZIP 解压到普通文件夹。
3. 打开解压后的文件夹。
4. 运行 `start.bat`。
5. 等待浏览器打开 `http://127.0.0.1:5000/admin`。
6. 在设置中确认 `PalWorldSettings.ini` 里的 `RESTAPIEnabled=True`，然后输入 `AdminPassword` 的值。
7. 点击 `应用`。
8. 将管理页面显示的公开 Live Map 地址分享给玩家。

### 默认设置

- `poll_interval_seconds`: `3`
- `history_limit`: `15`

### 主要说明

- 管理页面只能在同一台 PC 上打开。
- 公开 Live Map 页面支持语言切换。
- 管理页面也支持语言切换。
- 玩家上线和离线记录会自动保存。
- 你也可以使用 `your-domain:5000` 这样的域名地址，而不是直接使用 IP。

### 主要文件

- `start.bat`: 启动 Live Map
- `app.py`: 后端服务器
- `config.json`: 可编辑设置文件
- `static/`: Web 文件
- `python/`: 已包含的便携版 Python 运行环境
- `LICENSE`: CC0 许可正文
- `COPYRIGHT-CC0.txt`: 作者与 CC0 说明文件
