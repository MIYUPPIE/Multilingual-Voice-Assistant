@echo off
REM Multilingual Voice Assistant Setup Script for Windows
REM This script automates the setup process

setlocal enabledelayedexpansion

echo.
echo 🌍 Multilingual Voice Assistant - Setup Script (Windows)
echo ================================================== 
echo.

REM Check Python
echo ✓ Checking Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python not found. Please install Python 3.8 or higher
    echo    Download from: https://www.python.org/downloads/
    pause
    exit /b 1
)
for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo   Found Python %PYTHON_VERSION%

REM Check FFmpeg
echo.
echo ✓ Checking FFmpeg...
ffmpeg -version >nul 2>&1
if errorlevel 1 (
    echo ❌ FFmpeg not found. Please install FFmpeg:
    echo    https://ffmpeg.org/download.html
    echo    or use: choco install ffmpeg (if you have Chocolatey)
    pause
    exit /b 1
)
echo   Found FFmpeg

REM Create virtual environment
echo.
echo ✓ Creating Python virtual environment...
if exist venv (
    echo   Virtual environment already exists
) else (
    python -m venv venv
    echo   Created venv\
)

REM Activate virtual environment
echo ✓ Activating virtual environment...
call venv\Scripts\activate.bat

REM Upgrade pip
echo ✓ Upgrading pip...
python -m pip install --upgrade pip >nul 2>&1

REM Install dependencies
echo ✓ Installing Python dependencies...
echo   This may take a few minutes...
pip install -r requirements.txt >nul 2>&1
if errorlevel 1 (
    echo   ⚠️  Some packages may have failed to install
    echo   Continuing anyway...
)

REM Setup .env
echo.
echo ✓ Setting up environment configuration...
if exist .env (
    echo   .env file already exists
) else (
    if exist .env.example (
        copy .env.example .env >nul
        echo   Created .env from template
    ) else (
        echo   ⚠️  .env.example not found
    )
)

REM Create audio_files directory
echo ✓ Creating audio files directory...
if not exist audio_files mkdir audio_files

REM Test imports
echo.
echo ✓ Testing imports...
python -c "import whisper, openai, sounddevice, pyttsx3; print('  All imports successful ✓')" 2>nul
if errorlevel 1 (
    echo   ⚠️  Some imports may be missing
)

REM Summary
echo.
echo ==================================================
echo ✓ Setup Complete!
echo ==================================================
echo.
echo 📝 Next steps:
echo   1. Edit .env file and add your OpenAI API key:
echo      - Open: .env
echo      - Add: OPENAI_API_KEY=sk-your-key-here
echo.
echo   2. Test the installation:
echo      python main.py --test
echo.
echo   3. Start interactive mode:
echo      python main.py --language yoruba
echo.
echo 📚 For more information, see SETUP.md
echo.
echo 🚀 Ready to go!
echo.
pause
