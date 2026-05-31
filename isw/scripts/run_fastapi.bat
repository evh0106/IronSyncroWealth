@echo off
setlocal

set "BASE_DIR=%~dp0.."
set "VENV_PYTHON=%BASE_DIR%\.venv\Scripts\python.exe"

if not exist "%VENV_PYTHON%" (
    echo [ERROR] Virtual environment python not found: "%VENV_PYTHON%"
    echo [HINT] Run these commands first:
    echo        cd /d "%BASE_DIR%"
    echo        python -m venv .venv
    echo        .\.venv\Scripts\Activate.ps1
    echo        pip install fastapi "uvicorn[standard]" pydantic
    exit /b 1
)

cd /d "%BASE_DIR%"
set "PYTHONPATH=%BASE_DIR%\src"
"%VENV_PYTHON%" -m uvicorn src.main:app --host 0.0.0.0 --port 8010 --reload
