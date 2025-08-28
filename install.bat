@echo off
echo Installing War Thunder Voice Control...

:: Check if Python is installed
python --version > nul 2>&1
if errorlevel 1 (
    echo Python is not installed! Please install Python 3.x from https://www.python.org/downloads/
    pause
    exit /b 1
)

:: Create virtual environment if it doesn't exist
if not exist myenv (
    echo Creating virtual environment...
    python -m venv myenv
)

:: Activate virtual environment and install packages
echo Installing required packages...
call myenv\Scripts\activate.bat
pip install -r requirements.txt

echo.
echo Installation complete! You can now run start.bat to launch the program.
pause
