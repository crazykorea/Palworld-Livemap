@echo off
setlocal
cd /d "%~dp0"

set "PYTHON_EXE=%~dp0python\python.exe"
if exist "%PYTHON_EXE%" (
    set "RUNNER=%PYTHON_EXE%"
) else (
    set "RUNNER=python"
)

start "" cmd /c "timeout /t 2 >nul && start http://127.0.0.1:5000/admin"
"%RUNNER%" app.py
