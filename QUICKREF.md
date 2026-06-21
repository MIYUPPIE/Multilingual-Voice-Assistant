# 📖 Quick Reference Guide

## 🚀 Quick Start Commands

```bash
# Setup (first time)
python setup.py

# Edit configuration
nano .env

# Run in Yoruba
python main.py --language yoruba

# Run in Hausa
python main.py --language hausa

# Run in Igbo
python main.py --language igbo

# Test mode
python main.py --test
```

## 🎤 During Conversation

| Action | How |
|--------|-----|
| **Speak** | Just say something naturally |
| **Switch Language** | Say "switch to hausa" or mention language name |
| **Quit** | Say "quit", "exit", "bye", or "goodbye" |
| **Repeat** | Speak clearly again |

## ⚙️ Configuration Files

### `.env` - API and Settings
```env
OPENAI_API_KEY=sk-...
DEFAULT_LANGUAGE=yoruba
WHISPER_MODEL=base
```

### `config.py` - Language & Model Settings
```python
WHISPER_MODEL = "base"  # tiny, base, small, medium, large
SUPPORTED_LANGUAGES = {"yoruba", "hausa", "igbo"}
```

## 🗣️ Languages Quick Info

| Language | Code | Greeting | Location |
|----------|------|----------|----------|
| Yoruba | `yoruba` | Báwo ni? | Nigeria |
| Hausa | `hausa` | Sannu! | Nigeria, Niger |
| Igbo | `igbo` | Kedu? | Nigeria |

## 📂 Important Files

```
main.py           - Run this to start
config.py         - Change settings here
.env             - Add API key here
SETUP.md         - Detailed help
README.md        - Full documentation
```

## 🔧 Common Settings

### Whisper Model
- **tiny** - Fastest (~40MB)
- **base** - Recommended (~140MB) ← START HERE
- **small** - Better quality (~465MB)
- **medium** - High quality (~1.4GB)
- **large** - Best quality (~2.9GB)

### Speech Rate (TTS)
```python
TTS_CONFIG = {"rate": 120}  # Words per minute
```

### Conversation Memory
```python
YARNGPT_CONFIG = {"conversation_memory_limit": 10}  # Messages to remember
```

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| "No API key" | Add `OPENAI_API_KEY` to `.env` |
| "FFmpeg not installed" | `brew install ffmpeg` (macOS) or apt-get install ffmpeg (Linux) |
| "No audio input" | Check microphone permissions |
| "API rate limit" | Wait or upgrade your plan |
| "Poor audio quality" | Use larger Whisper model |
| "No response" | Check internet connection |

## 📝 File Structure

```
multilang/
├── main.py              ← Run this
├── config.py            ← Edit settings
├── .env                 ← Add API key
├── SETUP.md             ← Detailed setup
├── README.md            ← Documentation
├── FEATURES.md          ← Feature list
└── audio_files/         ← Generated audio
```

## 💻 Python Commands

```python
# Import and create
from main import MultilingualVoiceAssistant
assistant = MultilingualVoiceAssistant(language="yoruba")

# One interaction
assistant.chat()

# Manual control
text = assistant.listen()
response = assistant.think(text)
assistant.speak(response)

# Switch language
assistant.set_language("hausa")

# Clean up
assistant.cleanup()
```

## 🎯 Example Sentences

### Yoruba (Yorùbá)
- "Báwo ni?" - How are you?
- "Kin yi lomo yi o?" - What's this?
- "O dàa" - It's good

### Hausa (Hausa)
- "Sannu!" - Hello
- "Ina kwana?" - How was your night?
- "Na gida" - It's fine

### Igbo (Igbo)
- "Kedu?" - How are you?
- "Olee onu?" - What's the matter?
- "Ndewo oo" - Goodbye (respectful)

## 📊 API Usage

OpenAI pricing (approximate):
- gpt-3.5-turbo: $0.50 per 1M tokens
- gpt-4: $3.00 per 1M tokens
- Whisper: $0.02 per 1 hour audio

## 🔐 Security Checklist

- ✅ Keep `.env` file secret
- ✅ Don't share API keys
- ✅ Add `.env` to `.gitignore`
- ✅ Rotate keys periodically
- ✅ Use environment variables

## 📞 Getting Help

1. Check **SETUP.md** for detailed setup
2. See **README.md** for full documentation
3. Review **FEATURES.md** for capabilities
4. Read **config.py** comments for options

## 🚀 Performance Tips

1. Start with `base` Whisper model
2. Keep `conversation_memory_limit` low (5-10)
3. Use `gpt-3.5-turbo` for faster responses
4. Monitor token usage regularly
5. Cache common responses

## ⌚ Recording Duration

Default: 10 seconds

```python
python main.py --language yoruba
# Records for 10 seconds by default
# You can change in config.py
```

## 🎓 Learning Resources

- [OpenAI API](https://platform.openai.com/docs)
- [Whisper Docs](https://github.com/openai/whisper)
- [Yoruba Learning](https://www.youtube.com/c/YorubaEnglishTV)
- [Hausa Learning](https://www.bbc.com/pidgin)

## 💡 Quick Tips

- Use clear, natural speech
- Reduce background noise
- Maintain reasonable pace
- Be patient with responses
- Start with shorter interactions

## 🎯 Next Steps

1. Run `python setup.py`
2. Add API key to `.env`
3. Run `python main.py --test`
4. Try `python main.py --language yoruba`
5. Explore different languages

## 📈 Monitoring

Check API usage:
1. Visit https://platform.openai.com/account/usage/overview
2. Monitor token consumption
3. Manage API keys at https://platform.openai.com/api-keys

---

**Need more help?** Check the main README.md or SETUP.md files!
