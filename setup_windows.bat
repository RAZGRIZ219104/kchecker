@echo off
REM Windows Setup Script for Keyboard Checker
REM Run this script as Administrator for best results

echo Installing Keyboard Checker for Windows...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

echo Python detected, proceeding with setup...
echo.

REM Create virtual environment
echo Creating virtual environment...
python -m venv .venv
if errorlevel 1 (
    echo ERROR: Failed to create virtual environment
    pause
    exit /b 1
)

REM Activate virtual environment
echo Activating virtual environment...
call .venv\Scripts\activate.bat

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip

REM Install requirements
echo Installing required packages...
pip install -r requirements.txt

echo.
echo Setup complete! 
echo.
echo To run the keyboard checker:
echo   1. Open Command Prompt as Administrator (recommended)
echo   2. Navigate to this folder
echo   3. Run: .venv\Scripts\activate.bat
echo   4. Run: python main.py          (cross-platform version)
echo   5. Or:   python wversion.py     (Windows API version)
echo   6. Or:   python keyboard_lib_version.py (keyboard library)
echo.
echo Press any key to exit...
pause >nul
