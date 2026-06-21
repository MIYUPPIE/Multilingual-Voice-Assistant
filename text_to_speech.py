"""
Text-to-Speech module for audio output
"""

import pyttsx3
from config import SUPPORTED_LANGUAGES, TTS_CONFIG


class TextToSpeech:
    """Handle text-to-speech conversion"""
    
    def __init__(self):
        """Initialize text-to-speech engine"""
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', TTS_CONFIG['rate'])
        self.engine.setProperty('volume', TTS_CONFIG['volume'])
    
    def speak(self, text: str, language: str = "yoruba") -> None:
        """
        Convert text to speech and play
        
        Args:
            text: Text to convert to speech
            language: Language code (yoruba, hausa, igbo)
        """
        try:
            if language not in SUPPORTED_LANGUAGES:
                raise ValueError(f"Unsupported language: {language}. Supported: {list(SUPPORTED_LANGUAGES.keys())}")
            
            lang_name = SUPPORTED_LANGUAGES[language]["display_name"]
            print(f"\n🔊 Speaking in {lang_name}: {text}")
            
            self.engine.say(text)
            self.engine.runAndWait()
            print("✓ Speech complete")
        
        except Exception as e:
            print(f"❌ Error during speech: {e}")
            # Continue execution even if TTS fails
    
    def save_speech(self, text: str, filename: str, language: str = "yoruba") -> None:
        """
        Save text-to-speech as audio file
        
        Args:
            text: Text to convert
            filename: Output filename
            language: Language code
        """
        try:
            lang_name = SUPPORTED_LANGUAGES[language]["display_name"]
            print(f"\n💾 Saving speech in {lang_name} to {filename}")
            
            self.engine.save_to_file(text, filename)
            self.engine.runAndWait()
            print(f"✓ Saved to {filename}")
        
        except Exception as e:
            print(f"❌ Error saving speech: {e}")
            raise
