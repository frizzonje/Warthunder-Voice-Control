@echo off
echo Starting War Thunder Voice Control...

REM Check if virtual environment exists
if not exist myenv\Scripts\activate.bat (
    echo Virtual environment not found! Please run install.bat first.
    pause
    exit /b 1
)

REM Activate virtual environment
call myenv\Scripts\activate.bat

REM Check if settings.json exists
if not exist config\settings.json (
    echo settings.json not found! Please ensure config\settings.json exists and is configured.
    pause
    exit /b 1
)

REM Start the program
python src\main.py

REM If we get here, the program exited normally
pause
