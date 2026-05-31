@echo off
setlocal EnableDelayedExpansion

for %%I in ("%~dp0..") do set "BASE_DIR=%%~fI"
set "VENV_PYTHON=%BASE_DIR%\.venv\Scripts\python.exe"
set "SAMPLE_FILE=%BASE_DIR%\src\_sample\check_auth.py"

if not exist "%VENV_PYTHON%" (
    echo [ERROR] Virtual environment python not found: "%VENV_PYTHON%"
    exit /b 1
)

if not exist "%SAMPLE_FILE%" (
    echo [ERROR] Sample script not found: "%SAMPLE_FILE%"
    echo [INFO] Current skeleton does not include src\_sample\check_auth.py yet.
    exit /b 1
)

cd /d "%BASE_DIR%"
set "PYTHONPATH=%BASE_DIR%\src"
"%VENV_PYTHON%" "%SAMPLE_FILE%"
