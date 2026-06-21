# 🌍 Multilingual Voice Assistant Setup Guide

A sophisticated multilingual voice assistant combining **Whisper** (speech-to-text), **OpenAI GPT** (language understanding), and **YarnGPT** (advanced prompting) for Yoruba, Hausa, and Igbo languages.

## 📋 Prerequisites

- **Python 3.8+** (3.10+ recommended)
- **FFmpeg** (required for audio processing)
- **OpenAI API Key** (get from https://platform.openai.com/api-keys)
- **Microphone** for audio input

## 🚀 Quick Start

### 1. Install FFmpeg

**Ubuntu/Debian:**
```bash
sudo apt-get install ffmpeg
```

**macOS:**
```bash
brew install ffmpeg
```

**Windows:**
```bash
choco install ffmpeg
# or download from https://ffmpeg.org/download.html
```

### 2. Clone and Setup Project

```bash
# Navigate to project directory
cd /home/okhub/Documents/PROJECTS/multilang

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Linux/macOS:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure Environment

```bash
# Copy example configuration
cp .env.example .env

# Edit .env with your settings
nano .env
```

**Add your OpenAI API key:**
```env
OPENAI_API_KEY=sk-your-actual-api-key-here
```

### 5. Run the Assistant

```bash
# Interactive mode (start conversation)
python main.py --language yoruba

# Test mode (with sample inputs)
python main.py --language yoruba --test

# Other languages
python main.py --language hausa
python main.py --language igbo
```

## 🎯 Supported Languages

1. **Yoruba** (Yorùbá) - Nigeria
   - Code: `yoruba`
   - Whisper code: `yo`
   - Default greeting: "Báwo ni?"

2. **Hausa** (Hausa) - Nigeria & Niger
   - Code: `hausa`
   - Whisper code: `ha`
   - Default greeting: "Sannu!"

3. **Igbo** (Igbo) - Nigeria
   - Code: `igbo`
   - Whisper code: `ig`
   - Default greeting: "Kedu?"

## 🧠 YarnGPT Integration

YarnGPT-style techniques enhance the assistant with:

- ✅ **Context Awareness** - Maintains conversation history
- ✅ **Cultural Context** - Understands cultural nuances
- ✅ **Natural Language** - Uses culturally appropriate greetings
- ✅ **Memory Management** - Intelligent conversation history
- ✅ **Advanced Prompting** - Multi-turn conversation support

### Enable/Disable YarnGPT

```python
# In main.py or config
YARNGPT_CONFIG = {
    "enabled": True,  # Set to False to disable
    "context_awareness": True,
    "cultural_context": True,
}
```

## 📁 Project Structure

```
multilang/
├── main.py                 # Main application entry point
├── config.py              # Configuration and constants
├── language_model.py      # GPT + YarnGPT integration
├── speech_to_text.py      # Whisper integration
├── text_to_speech.py      # TTS output
├── audio_handler.py       # Audio recording/playback
├── requirements.txt       # Python dependencies
├── .env.example          # Environment template
├── SETUP.md              # This file
└── audio_files/          # Generated audio files
```

## 🎤 How It Works

### Workflow: Listen → Understand → Respond → Speak

```
User speaks (in Yoruba/Hausa/Igbo)
    ↓
[Whisper] Converts speech to text
    ↓
[YarnGPT] Enhances input with cultural context
    ↓
[ChatGPT] Generates response (in native language)
    ↓
[pyttsx3] Converts response back to speech
    ↓
User hears response
```

## 🔧 Configuration Options

### Audio Settings (`config.py`)

```python
AUDIO_CONFIG = {
    "sample_rate": 16000,      # Hz
    "channels": 1,             # Mono
    "duration": 10,            # Seconds
    "format": "wav"
}
```

### Whisper Model Selection

```python
WHISPER_MODEL = "base"  # tiny, base, small, medium, large
```

- **tiny**: Fastest, lowest quality (~40MB)
- **base**: Good balance (~140MB) - Recommended
- **small**: Better accuracy (~465MB)
- **medium**: High accuracy (~1.4GB)
- **large**: Best accuracy (~2.9GB)

### Text-to-Speech Settings

```python
TTS_CONFIG = {
    "rate": 120,      # Words per minute
    "volume": 1.0     # 0.0 to 1.0
}
```

## 💡 Usage Examples

### Interactive Mode

```bash
python main.py --language yoruba
```

Commands:
- Speak naturally in the selected language
- Say "quit" or "exit" to end
- Mention "hausa" or "igbo" to switch languages

Example:
```
User: "Bawo ni o? Kin yi lomo yi o?"
Assistant: [Responds in Yoruba]
User: "Switch to hausa"
Assistant: [Changes language to Hausa]
```

### Test Mode

```bash
python main.py --language yoruba --test
```

Runs with predefined test inputs for each language.

### Programmatic Usage

```python
from main import MultilingualVoiceAssistant

# Create assistant
assistant = MultilingualVoiceAssistant(language="yoruba")

# Single turn
user_input = assistant.listen()           # Record and transcribe
response = assistant.think(user_input)    # Generate response
assistant.speak(response)                 # Play response

# Or use single method
assistant.chat()  # One complete cycle

# Switch languages
assistant.set_language("hausa")

# Clean up
assistant.cleanup()
```

## 🛠️ Troubleshooting

### "No module named 'openai'"
```bash
pip install openai
```

### "No module named 'whisper'"
```bash
pip install openai-whisper
```

### "ffmpeg not found"
Install FFmpeg for your OS (see Prerequisites)

### No audio input detected
- Check microphone is plugged in and enabled
- Verify permissions: `python -c "import sounddevice; print(sounddevice.query_devices())"`
- Try increasing recording duration in config

### API Rate Limit
- Wait a moment before trying again
- Upgrade your OpenAI plan for higher limits
- Use `gpt-3.5-turbo` instead of `gpt-4`

### Language not recognized
- Ensure FFmpeg is installed
- Try "tiny" or "base" Whisper model
- Check language code in config

### Poor response quality
- Longer context (increase `CONVERSATION_MEMORY_LIMIT`)
- Use larger Whisper model
- Ensure good audio quality
- Check OpenAI API key validity

## 📊 Requirements Summary

### System

- 4GB RAM minimum (8GB recommended)
- 5GB disk space for models
- Stable internet connection
- Microphone and speakers

### Python Packages

- `openai-whisper` - Speech recognition
- `openai` - GPT access
- `pyttsx3` - Text-to-speech
- `sounddevice` - Audio input
- `soundfile` - Audio file handling
- `python-dotenv` - Environment management

## 🔐 Security

- **Keep `.env` file private** - Never commit it to git
- **Rotate API keys regularly**
- **Use environment variables** for sensitive data
- **Add `.env` to `.gitignore`**

```bash
# .gitignore
.env
*.pyc
audio_files/
```

## 🚀 Performance Tips

1. **Use Smaller Whisper Model**: Start with "tiny" or "base"
2. **Cache Responses**: Implement response caching for common queries
3. **Batch Processing**: Use multi-turn conversations
4. **Optimize Audio**: Use mono, 16kHz sample rate
5. **Monitor API Usage**: Track OpenAI token usage

## 📚 Advanced Configuration

### Custom System Prompts

Edit `config.py`:
```python
SYSTEM_PROMPTS = {
    "yoruba": "Your custom Yoruba prompt...",
    "hausa": "Your custom Hausa prompt...",
    "igbo": "Your custom Igbo prompt...",
}
```

### Cultural Preambles

Customize greetings:
```python
CULTURAL_PREAMBLES = {
    "yoruba": {
        "greeting": "Báwo ni o?",
        "farewell": "Ó dàbò o",
        # ... more entries
    }
}
```

### YarnGPT Advanced Settings

```python
YARNGPT_CONFIG = {
    "enabled": True,
    "context_awareness": True,
    "cultural_context": True,
    "conversation_memory_limit": 10,
    "max_response_attempts": 3,
    "temperature_for_creativity": 0.7,
    "temperature_for_accuracy": 0.3,
}
```

## 📞 Support & Resources

- **OpenAI Documentation**: https://platform.openai.com/docs
- **Whisper GitHub**: https://github.com/openai/whisper
- **FFmpeg Documentation**: https://ffmpeg.org/documentation.html
- **pyttsx3 Docs**: https://pyttsx3.readthedocs.io/

## 📝 License

This project is provided as-is for educational and personal use.

## 🎓 Learning Resources

- Yoruba Resources: https://www.youtube.com/c/YorubaEnglishTV
- Hausa Resources: https://www.bbc.com/pidgin
- Igbo Resources: https://www.igboonline.com

---

**Happy coding! 🚀**

For issues or improvements, please open an issue or submit a pull request.
