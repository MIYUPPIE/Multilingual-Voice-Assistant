#!/usr/bin/env python3
"""
Multilingual Voice Assistant - Setup Script
Platform-independent setup using Python
"""

import os
import sys
import subprocess
import shutil
import platform
from pathlib import Path


class Setup:
    """Setup assistant for multilingual voice project"""
    
    def __init__(self):
        self.project_dir = Path(__file__).parent
        self.venv_dir = self.project_dir / "venv"
        self.python_cmd = "python3" if shutil.which("python3") else "python"
        self.system = platform.system()
    
    def print_header(self):
        """Print welcome header"""
        print("\n" + "="*50)
        print("🌍 Multilingual Voice Assistant - Setup")
        print("="*50 + "\n")
    
    def check_python(self):
        """Check Python version"""
        print("✓ Checking Python version...")
        try:
            result = subprocess.run(
                [self.python_cmd, "--version"],
                capture_output=True,
                text=True
            )
            version = result.stdout.strip()
            print(f"  Found {version}\n")
            return True
        except Exception as e:
            print(f"  ❌ Error: {e}\n")
            return False
    
    def check_ffmpeg(self):
        """Check FFmpeg installation"""
        print("✓ Checking FFmpeg...")
        if shutil.which("ffmpeg"):
            print("  Found FFmpeg\n")
            return True
        else:
            print("  ❌ FFmpeg not found!")
            if self.system == "Darwin":
                print("  Install on macOS: brew install ffmpeg")
            elif self.system == "Windows":
                print("  Install on Windows: choco install ffmpeg")
            else:
                print("  Install on Linux: sudo apt-get install ffmpeg")
            print()
            return False
    
    def create_venv(self):
        """Create virtual environment"""
        print("✓ Creating virtual environment...")
        if self.venv_dir.exists():
            print("  Virtual environment already exists\n")
            return True
        
        try:
            subprocess.run(
                [self.python_cmd, "-m", "venv", str(self.venv_dir)],
                check=True
            )
            print("  Created venv/\n")
            return True
        except Exception as e:
            print(f"  ❌ Error: {e}\n")
            return False
    
    def install_packages(self):
        """Install Python packages"""
        print("✓ Installing Python packages...")
        print("  This may take a few minutes...\n")
        
        # Determine pip path
        if self.system == "Windows":
            pip_cmd = self.venv_dir / "Scripts" / "pip"
        else:
            pip_cmd = self.venv_dir / "bin" / "pip"
        
        try:
            # Upgrade pip
            subprocess.run(
                [str(pip_cmd), "install", "--upgrade", "pip"],
                check=True,
                capture_output=True
            )
            
            # Install requirements
            subprocess.run(
                [str(pip_cmd), "install", "-r", "requirements.txt"],
                check=True,
                capture_output=True
            )
            
            print("  ✓ Packages installed successfully\n")
            return True
        except Exception as e:
            print(f"  ❌ Error: {e}\n")
            return False
    
    def setup_env_file(self):
        """Setup .env file"""
        print("✓ Setting up environment configuration...")
        
        env_file = self.project_dir / ".env"
        env_example = self.project_dir / ".env.example"
        
        if env_file.exists():
            print("  .env file already exists\n")
        elif env_example.exists():
            shutil.copy(env_example, env_file)
            print("  Created .env from template\n")
        else:
            print("  ⚠️  .env.example not found\n")
    
    def create_audio_dir(self):
        """Create audio files directory"""
        print("✓ Creating audio files directory...")
        audio_dir = self.project_dir / "audio_files"
        audio_dir.mkdir(exist_ok=True)
        print()
    
    def test_imports(self):
        """Test Python imports"""
        print("✓ Testing imports...")
        
        imports_to_test = [
            "whisper",
            "openai",
            "sounddevice",
            "pyttsx3"
        ]
        
        all_ok = True
        for module in imports_to_test:
            try:
                __import__(module)
            except ImportError:
                print(f"  ⚠️  Could not import {module}")
                all_ok = False
        
        if all_ok:
            print("  ✓ All imports successful\n")
        else:
            print()
        
        return True
    
    def print_next_steps(self):
        """Print next steps"""
        print("="*50)
        print("✓ Setup Complete!")
        print("="*50 + "\n")
        
        print("📝 Next steps:")
        print("  1. Edit .env file with your OpenAI API key:")
        print("     # Add: OPENAI_API_KEY=sk-your-key-here\n")
        
        print("  2. Test the installation:")
        print("     python main.py --test\n")
        
        print("  3. Start interactive mode:")
        print("     python main.py --language yoruba\n")
        
        print("📚 For more information, see SETUP.md\n")
        print("🚀 Ready to go!\n")
    
    def run(self):
        """Run complete setup"""
        self.print_header()
        
        # Check requirements
        if not self.check_python():
            print("Python is required. Please install Python 3.8+")
            return False
        
        if not self.check_ffmpeg():
            response = input("Continue without FFmpeg? (y/n): ").lower()
            if response != 'y':
                return False
        
        # Setup
        if not self.create_venv():
            return False
        
        if not self.install_packages():
            return False
        
        self.setup_env_file()
        self.create_audio_dir()
        self.test_imports()
        self.print_next_steps()
        
        return True


if __name__ == "__main__":
    setup = Setup()
    success = setup.run()
    sys.exit(0 if success else 1)
