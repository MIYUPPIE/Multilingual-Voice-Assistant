#!/bin/bash

# Multilingual Voice Assistant Setup Script
# This script automates the setup process

set -e  # Exit on error

echo "🌍 Multilingual Voice Assistant - Setup Script"
echo "=================================================="
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check Python version
echo "✓ Checking Python version..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
    echo "  Found Python $PYTHON_VERSION"
else
    echo -e "${RED}❌ Python3 not found. Please install Python 3.8 or higher.${NC}"
    exit 1
fi

# Check FFmpeg
echo ""
echo "✓ Checking FFmpeg..."
if command -v ffmpeg &> /dev/null; then
    FFMPEG_VERSION=$(ffmpeg -version 2>&1 | head -n1 | cut -d' ' -f3)
    echo "  Found FFmpeg"
else
    echo -e "${RED}❌ FFmpeg not found. Please install FFmpeg:${NC}"
    echo "  Ubuntu/Debian: sudo apt-get install ffmpeg"
    echo "  macOS: brew install ffmpeg"
    echo "  Windows: choco install ffmpeg"
    exit 1
fi

# Create virtual environment
echo ""
echo "✓ Creating Python virtual environment..."
if [ -d "venv" ]; then
    echo "  Virtual environment already exists"
else
    python3 -m venv venv
    echo "  Created venv/"
fi

# Activate virtual environment
echo "✓ Activating virtual environment..."
source venv/bin/activate 2>/dev/null || . venv/Scripts/activate 2>/dev/null || true

# Upgrade pip
echo "✓ Upgrading pip..."
python -m pip install --upgrade pip > /dev/null 2>&1

# Install dependencies
echo "✓ Installing Python dependencies..."
echo "  This may take a few minutes..."
pip install -r requirements.txt > /dev/null 2>&1

# Create .env file if it doesn't exist
echo ""
echo "✓ Setting up environment configuration..."
if [ -f ".env" ]; then
    echo "  .env file already exists"
else
    if [ -f ".env.example" ]; then
        cp .env.example .env
        echo "  Created .env from template"
    else
        echo "  ⚠️  .env.example not found"
    fi
fi

# Create audio_files directory
echo "✓ Creating audio files directory..."
mkdir -p audio_files

# Test imports
echo ""
echo "✓ Testing imports..."
python -c "
try:
    import whisper
    import openai
    import sounddevice
    import pyttsx3
    print('  All imports successful ✓')
except ImportError as e:
    print(f'  Warning: {e}')
" 2>/dev/null || echo "  ⚠️  Some imports may be missing"

# Summary
echo ""
echo "=================================================="
echo -e "${GREEN}✓ Setup Complete!${NC}"
echo "=================================================="
echo ""
echo "📝 Next steps:"
echo "  1. Edit .env file and add your OpenAI API key:"
echo "     nano .env"
echo "     # Add: OPENAI_API_KEY=sk-your-key-here"
echo ""
echo "  2. Test the installation:"
echo "     python main.py --test"
echo ""
echo "  3. Start interactive mode:"
echo "     python main.py --language yoruba"
echo ""
echo "📚 For more information, see SETUP.md"
echo ""
echo "🚀 Ready to go!"
