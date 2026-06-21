"""
Main application for multilingual voice assistant combining Whisper, GPT, and TTS
"""

import os
import sys
from typing import Optional
from dotenv import load_dotenv

from audio_handler import AudioHandler
from speech_to_text import SpeechToText
from text_to_speech import TextToSpeech
from language_model import LanguageModel, YarnGPTStyle
from config import SUPPORTED_LANGUAGES


class MultilingualVoiceAssistant:
    """Main voice assistant combining all components"""
    
    def __init__(self, language: str = "yoruba"):
        """
        Initialize the voice assistant
        
        Args:
            language: Language code (yoruba, hausa, igbo)
        """
        # Load environment variables
        load_dotenv()
        
        if language not in SUPPORTED_LANGUAGES:
            raise ValueError(f"Unsupported language: {language}. Supported: {list(SUPPORTED_LANGUAGES.keys())}")
        
        self.language = language
        self.lang_name = SUPPORTED_LANGUAGES[language]["display_name"]
        
        print(f"\n{'='*60}")
        print(f"🌍 Multilingual Voice Assistant - {self.lang_name}")
        print(f"{'='*60}\n")
        
        # Initialize components
        self.audio_handler = AudioHandler()
        self.speech_to_text = SpeechToText()
        self.text_to_speech = TextToSpeech()
        self.language_model = LanguageModel()
        self.conversation_history = []
    
    def set_language(self, language: str):
        """Change the active language"""
        if language not in SUPPORTED_LANGUAGES:
            raise ValueError(f"Unsupported language: {language}")
        self.language = language
        self.lang_name = SUPPORTED_LANGUAGES[language]["display_name"]
        print(f"\n✓ Language changed to {self.lang_name}")
    
    def listen(self, duration: int = 10) -> str:
        """
        Listen to user speech and convert to text
        
        Args:
            duration: Recording duration in seconds
            
        Returns:
            Transcribed text
        """
        try:
            # Record audio
            audio_file = self.audio_handler.record_audio(duration)
            
            # Convert to text
            text = self.speech_to_text.transcribe(audio_file, self.language)
            
            # Clean up audio file
            os.remove(audio_file)
            
            return text
        
        except Exception as e:
            print(f"❌ Error in listen: {e}")
            return ""
    
    def think(self, user_input: str) -> str:
        """
        Process user input and generate response
        
        Args:
            user_input: User's input text
            
        Returns:
            Generated response
        """
        try:
            # Add to conversation history
            self.conversation_history.append({
                "role": "user",
                "content": user_input
            })
            
            # Generate response
            response = self.language_model.generate_response(user_input, self.language)
            
            # Add to history
            self.conversation_history.append({
                "role": "assistant",
                "content": response
            })
            
            return response
        
        except Exception as e:
            print(f"❌ Error in think: {e}")
            return "I apologize, but I encountered an error processing your request."
    
    def speak(self, text: str):
        """
        Convert text to speech and play
        
        Args:
            text: Text to speak
        """
        try:
            self.text_to_speech.speak(text, self.language)
        except Exception as e:
            print(f"❌ Error in speak: {e}")
    
    def chat(self, duration: int = 10) -> bool:
        """
        Single turn conversation: Listen -> Think -> Speak
        
        Args:
            duration: Recording duration in seconds
            
        Returns:
            True if successful, False if user wants to quit
        """
        try:
            print(f"\n{'─'*60}")
            
            # Listen
            user_input = self.listen()
            
            if not user_input:
                print("⚠️  No speech detected. Please try again.")
                return True
            
            # Check for quit command
            if user_input.lower() in ["quit", "exit", "bye", "goodbye"]:
                print("\n👋 Goodbye! Thank you for using the Multilingual Voice Assistant.")
                return False
            
            # Check for language change command
            for lang_code, lang_info in SUPPORTED_LANGUAGES.items():
                if lang_code.lower() in user_input.lower():
                    self.set_language(lang_code)
                    self.speak(f"Language changed to {self.lang_name}")
                    return True
            
            # Think (generate response)
            response = self.think(user_input)
            
            # Speak response
            self.speak(response)
            
            return True
        
        except KeyboardInterrupt:
            print("\n\n👋 Interrupted by user.")
            return False
        except Exception as e:
            print(f"❌ Error in chat: {e}")
            return True
    
    def interactive_loop(self):
        """Run interactive conversation loop"""
        print(f"\n💬 Starting interactive mode in {self.lang_name}")
        print("📝 Commands:")
        print("  - Say 'quit' or 'exit' to quit")
        print("  - Mention 'yoruba', 'hausa', or 'igbo' to switch languages")
        print("\n" + "="*60)
        
        try:
            while True:
                if not self.chat():
                    break
        
        finally:
            self.cleanup()
    
    def test_mode(self):
        """Test mode with predefined inputs"""
        print("\n🧪 Running in test mode with sample inputs...")
        
        test_inputs = {
            "yoruba": "Bawo ni o? Kin yi lomo yi o?",
            "hausa": "Sannu! Hana fita?",
            "igbo": "Kedu! Olee ine akwukwo?"
        }
        
        for language, test_input in test_inputs.items():
            print(f"\n{'='*60}")
            self.set_language(language)
            print(f"User input: {test_input}")
            
            response = self.think(test_input)
            print(f"Assistant: {response}")
        
        self.cleanup()
    
    def cleanup(self):
        """Clean up resources"""
        print("\n🧹 Cleaning up...")
        self.audio_handler.cleanup_audio_files()
        print("✓ Cleanup complete")


def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Multilingual Voice Assistant")
    parser.add_argument(
        "--language", 
        choices=list(SUPPORTED_LANGUAGES.keys()),
        default="yoruba",
        help="Language to use (default: yoruba)"
    )
    parser.add_argument(
        "--test",
        action="store_true",
        help="Run in test mode with sample inputs"
    )
    
    args = parser.parse_args()
    
    try:
        assistant = MultilingualVoiceAssistant(language=args.language)
        
        if args.test:
            assistant.test_mode()
        else:
            assistant.interactive_loop()
    
    except KeyboardInterrupt:
        print("\n\n👋 Interrupted by user. Exiting...")
    except Exception as e:
        print(f"\n❌ Fatal error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
