"""
Language configuration for multilingual voice assistant
"""

SUPPORTED_LANGUAGES = {
    "yoruba": {
        "code": "yo",
        "name": "Yoruba",
        "whisper_code": "yo",
        "display_name": "Yorùbá"
    },
    "hausa": {
        "code": "ha",
        "name": "Hausa",
        "whisper_code": "ha",
        "display_name": "Hausa"
    },
    "igbo": {
        "code": "ig",
        "name": "Igbo",
        "whisper_code": "ig",
        "display_name": "Igbo"
    }
}

# Audio settings
AUDIO_CONFIG = {
    "sample_rate": 16000,
    "channels": 1,
    "duration": 10,  # seconds
    "format": "wav"
}

# Whisper model size options: tiny, base, small, medium, large
WHISPER_MODEL = "base"

# OpenAI API configuration
OPENAI_API_CONFIG = {
    "model": "gpt-3.5-turbo",
    "temperature": 0.7,
    "max_tokens": 500
}

# System prompts for different languages with YarnGPT-style context
SYSTEM_PROMPTS = {
    "yoruba": """You are a respectful and knowledgeable Yoruba language assistant.
- Respond only in Yoruba language
- Show respect for Yoruba culture and traditions
- Use greetings appropriately (e.g., "Bawo ni", "Jọ o", "E kaaro")
- Keep responses concise and natural
- Include cultural context when appropriate
- Be helpful and friendly""",
    
    "hausa": """You are a respectful and knowledgeable Hausa language assistant.
- Respond only in Hausa language
- Show respect for Hausa culture and traditions
- Use appropriate greetings (e.g., "Sannu", "Sannu da aiki")
- Keep responses concise and natural
- Include cultural context when appropriate
- Be helpful and friendly""",
    
    "igbo": """You are a respectful and knowledgeable Igbo language assistant.
- Respond only in Igbo language
- Show respect for Igbo culture and traditions
- Use appropriate greetings (e.g., "Kedu", "Ndewo oo")
- Keep responses concise and natural
- Include cultural context when appropriate
- Be helpful and friendly"""
}

# YarnGPT Configuration - Advanced prompt engineering for better context awareness
YARNGPT_CONFIG = {
    "enabled": True,
    "context_awareness": True,
    "cultural_context": True,
    "conversation_memory_limit": 10,  # Number of previous messages to keep
    "max_response_attempts": 3,  # Retry failed responses
    "temperature_for_creativity": 0.7,
    "temperature_for_accuracy": 0.3,
}

# Cultural context preambles for YarnGPT
CULTURAL_PREAMBLES = {
    "yoruba": {
        "greeting": "Báwo ni o? E kaaro",
        "farewell": "Ó dàbò o. Ẹ pamọ́",
        "affirmation": "O dàa, bí ẹ́ bá rora",
        "question_intro": "Báwo ni ẹ̀ wọ̀?",
        "cultural_note": "In Yoruba culture, respect and politeness are paramount"
    },
    "hausa": {
        "greeting": "Sannu! Da yamma",
        "farewell": "Sai an jima",
        "affirmation": "I santsi, alhamdulilahi",
        "question_intro": "Ina kwana?",
        "cultural_note": "In Hausa culture, greetings and proper etiquette are very important"
    },
    "igbo": {
        "greeting": "Ndewo! Kedu",
        "farewell": "Ugbua m na-aga. Ndewo oo",
        "affirmation": "Enyim, daalụ",
        "question_intro": "Olee onu?",
        "cultural_note": "In Igbo culture, Ubuntu philosophy - I am because we are"
    }
}

# Text-to-speech settings
TTS_CONFIG = {
    "rate": 120,  # words per minute
    "volume": 1.0
}
