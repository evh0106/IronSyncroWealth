@echo off
setlocal EnableDelayedExpansion

REM Define the base directory
for %%I in ("%~dp0..") do set "BASE_DIR=%%~fI"

REM Activate the virtual environment
REM `call`은 환경을 활성화한 후에도 스크립트가 계속 실행되도록 하는 데 사용됩니다.
call %BASE_DIR%\.venv\Scripts\activate

REM Set the Python path
set PYTHONPATH=%BASE_DIR%\src

REM Run the Python app
python %BASE_DIR%\src\_sample\check_auth.py

REM Deactivate the virtual environment
deactivate