@echo off
setlocal

set "BASE_DIR=%~dp0.."

if not exist "%BASE_DIR%\scripts\run_fastapi.bat" (
    echo [ERROR] run_fastapi.bat not found.
    exit /b 1
)

call "%BASE_DIR%\scripts\run_fastapi.bat"
