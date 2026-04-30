@echo off
setlocal

set "BASE_DIR=%~dp0.."
set "VENV_PYTHON=%BASE_DIR%\.venv\Scripts\python.exe"

if not exist "%VENV_PYTHON%" (
    echo [ERROR] Virtual environment python not found: "%VENV_PYTHON%"
    exit /b 1
)

cd /d "%BASE_DIR%\src"
"%VENV_PYTHON%" -m uvicorn app.main:app --host 0.0.0.0 --port 8001 --reload@echo off
setlocal

set "BASE_DIR=%~dp0.."
set "VENV_PYTHON=%BASE_DIR%\.venv\Scripts\python.exe"

if not exist "%VENV_PYTHON%" (
    echo [ERROR] Virtual environment python not found: "%VENV_PYTHON%"
    exit /b 1
)

cd /d "%BASE_DIR%\src"
"%VENV_PYTHON%" -m uvicorn app.main:app --host 0.0.0.0 --port 8001 --reload