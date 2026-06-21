"""
Speech-to-Text module using OpenAI Whisper
"""

import whisper
from config import WHISPER_MODEL, SUPPORTED_LANGUAGES


class SpeechToText:
    """Handle speech-to-text conversion using Whisper"""
    
    def __init__(self, model_name: str = WHISPER_MODEL):
        """
        Initialize Whisper model
        
        Args:
            model_name: Model size (tiny, base, small, medium, large)
        """
        print(f"📥 Loading Whisper model: {model_name}")
        self.model = whisper.load_model(model_name)
        print("✓ Whisper model loaded successfully")
    
    def transcribe(self, audio_file: str, language: str = "yoruba") -> str:
        """
        Transcribe audio file to text
        
        Args:
            audio_file: Path to audio file
            language: Language code (yoruba, hausa, igbo)
            
        Returns:
            Transcribed text
        """
        try:
            if language not in SUPPORTED_LANGUAGES:
                raise ValueError(f"Unsupported language: {language}. Supported: {list(SUPPORTED_LANGUAGES.keys())}")
            
            lang_code = SUPPORTED_LANGUAGES[language]["whisper_code"]
            
            print(f"🎙️  Transcribing audio in {SUPPORTED_LANGUAGES[language]['display_name']}...")
            
            # Transcribe with specified language
            result = self.model.transcribe(
                audio_file,
                language=lang_code,
                verbose=False
            )
            
            text = result["text"].strip()
            print(f"✓ Transcribed text: {text}")
            
            return text
        
        except Exception as e:
            print(f"❌ Error transcribing audio: {e}")
            raise
