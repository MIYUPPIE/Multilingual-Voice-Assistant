# 🌍 Multilingual Voice Assistant

A powerful, culturally-aware AI voice assistant that speaks **Yoruba**, **Hausa**, and **Igbo** using advanced technologies:

- **🗣️ Speech Recognition**: OpenAI Whisper
- **🧠 Language Understanding**: OpenAI GPT + YarnGPT
- **🔊 Speech Synthesis**: pyttsx3
- **🎯 Cultural Context**: YarnGPT-style prompt engineering

## ✨ Features

✅ **Real-time Voice Interaction** - Speak in your native language  
✅ **Multi-language Support** - Yoruba, Hausa, Igbo  
✅ **Cultural Awareness** - Context-aware responses  
✅ **Conversation Memory** - Maintains chat history  
✅ **Easy Setup** - Automated installation scripts  
✅ **Production Ready** - Error handling & logging  

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- FFmpeg
- OpenAI API Key ([get one free](https://platform.openai.com/api-keys))

### Installation

```bash
# Clone/navigate to project
cd /path/to/multilang

# Automatic setup (recommended)
python setup.py

# OR manual setup
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

**Then add your OpenAI API key to `.env`:**
```env
OPENAI_API_KEY=sk-your-api-key-here
```

### Usage

```bash
# Interactive mode - choose language
python main.py --language yoruba

# Other languages
python main.py --language hausa
python main.py --language igbo

# Test mode
python main.py --test
```

## 🎯 How It Works

```
User speaks → Whisper transcribes → YarnGPT enhances → 
GPT responds → pyttsx3 speaks back → User hears response
```

### Example Interaction

```
🎤 Recording for 10 seconds... Speak now!
✓ Recording complete
🎙️  Transcribing audio in Yorùbá...
✓ Transcribed text: Bawo ni o?

🤖 Generating response in Yorùbá (YarnGPT-enhanced)...
✓ Response generated: Ọ dàa... [culturally appropriate response]

🔊 Speaking in Yorùbá: [Audio plays]
```

## 🌐 Supported Languages

| Language | Code | Greeting | Region |
|----------|------|----------|--------|
| **Yoruba** | `yoruba` | Báwo ni? | Nigeria |
| **Hausa** | `hausa` | Sannu! | Nigeria, Niger |
| **Igbo** | `igbo` | Kedu? | Nigeria |

## 📚 Documentation

- **[SETUP.md](SETUP.md)** - Detailed setup guide
- **[config.py](config.py)** - Configuration options
- **[main.py](main.py)** - Main application entry point

## 🧠 YarnGPT Integration

YarnGPT-style prompt engineering enhances the assistant with:

- **Context Awareness** - Remembers conversation history
- **Cultural Context** - Uses culturally appropriate language
- **Natural Responses** - Includes greetings, idioms, traditions
- **Multi-turn Support** - Maintains conversation flow
- **Error Handling** - Culturally appropriate error messages

### Configuration

```python
# In config.py
YARNGPT_CONFIG = {
    "enabled": True,
    "context_awareness": True,
    "cultural_context": True,
    "conversation_memory_limit": 10,
}
```

## 🔧 Project Structure

```
multilang/
├── main.py              # Application entry point
├── config.py            # Configuration & constants
├── language_model.py    # GPT + YarnGPT engine
├── speech_to_text.py    # Whisper integration
├── text_to_speech.py    # Audio output
├── audio_handler.py     # Recording/playback
├── setup.py             # Setup script (Python)
├── setup.sh             # Setup script (Linux/Mac)
├── setup.bat            # Setup script (Windows)
├── SETUP.md             # Detailed setup guide
├── README.md            # This file
└── requirements.txt     # Python dependencies
```

## 💡 Usage Examples

### Test Mode
```bash
python main.py --test
# Runs with predefined inputs for testing
```

### Interactive Conversation
```bash
python main.py --language yoruba

# In the prompt:
# Speak: "Bawo ni o? Kin yi lomo yi o?"
# Assistant responds in Yoruba
# Say "quit" to exit
# Say "hausa" to switch to Hausa
```

### Programmatic Usage
```python
from main import MultilingualVoiceAssistant

assistant = MultilingualVoiceAssistant(language="yoruba")

# Single conversation cycle
assistant.chat()  # Listen -> Think -> Speak

# Manual control
text = assistant.listen()      # Record and transcribe
response = assistant.think(text)    # Generate response
assistant.speak(response)      # Play audio

# Switch languages
assistant.set_language("hausa")

# Cleanup
assistant.cleanup()
```

## 🔐 Security

- ✅ Keep `.env` file private (add to `.gitignore`)
- ✅ Use environment variables for API keys
- ✅ Rotate API keys regularly
- ✅ Don't commit `.env` to version control

```bash
# .gitignore
.env
*.pyc
__pycache__/
audio_files/
venv/
```

## ⚙️ Configuration

### Audio Settings
```python
# config.py
AUDIO_CONFIG = {
    "sample_rate": 16000,    # Hz
    "channels": 1,           # Mono
    "duration": 10,          # Seconds
}
```

### Whisper Model Selection
- `tiny` (fastest, ~40MB)
- `base` (recommended, ~140MB)
- `small` (~465MB)
- `medium` (~1.4GB)
- `large` (best quality, ~2.9GB)

### Text-to-Speech
```python
TTS_CONFIG = {
    "rate": 120,    # Words per minute
    "volume": 1.0   # 0.0 to 1.0
}
```

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| `No module named 'openai'` | `pip install openai` |
| `FFmpeg not found` | Install FFmpeg for your OS |
| `No API key` | Add `OPENAI_API_KEY` to `.env` |
| `No audio input` | Check microphone permissions |
| `Poor quality` | Use larger Whisper model |

See [SETUP.md](SETUP.md#-troubleshooting) for more help.

## 📊 System Requirements

- **RAM**: 4GB minimum (8GB recommended)
- **Storage**: 5GB for models
- **Internet**: Stable connection (for API calls)
- **Audio**: Microphone & speakers

## 📦 Dependencies

```
openai-whisper  # Speech recognition
openai          # ChatGPT API
pyttsx3         # Text-to-speech
sounddevice     # Audio input
python-dotenv   # Environment config
```

[Full requirements.txt](requirements.txt)

## 🚀 Performance Tips

1. Start with `WHISPER_MODEL = "base"`
2. Use `temperature_for_accuracy` for precise responses
3. Keep conversation memory limit reasonable
4. Monitor OpenAI API usage
5. Cache common responses

## 🎓 Learning Resources

- [Yoruba Language](https://www.culturalsurvival.org/publications/cultural-survival-quarterly/yoruba)
- [Hausa Language](https://www.ethnologue.com/language/hau)
- [Igbo Language](https://www.igboonline.com)
- [OpenAI Docs](https://platform.openai.com/docs)
- [Whisper Docs](https://github.com/openai/whisper)

## 📝 License

This project is provided for educational and personal use.

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## 📞 Support

- Check [SETUP.md](SETUP.md) for detailed troubleshooting
- Review [config.py](config.py) for configuration options
- Check [main.py](main.py) for usage examples

## 🎉 Acknowledgments

Built with:
- [OpenAI Whisper](https://github.com/openai/whisper)
- [OpenAI GPT](https://openai.com)
- [pyttsx3](https://pyttsx3.readthedocs.io/)

---

**Get started now:**
```bash
python setup.py
nano .env  # Add your API key
python main.py --language yoruba
```

**Happy coding! 🚀**
