"""
Audio handling module for recording and playback
"""

import sounddevice as sd
import soundfile as sf
import numpy as np
from typing import Tuple
import os
from config import AUDIO_CONFIG


class AudioHandler:
    """Handle audio recording and playback"""
    
    def __init__(self):
        self.audio_dir = "audio_files"
        self._ensure_audio_dir()
    
    def _ensure_audio_dir(self):
        """Create audio directory if it doesn't exist"""
        if not os.path.exists(self.audio_dir):
            os.makedirs(self.audio_dir)
    
    def record_audio(self, duration: int = AUDIO_CONFIG["duration"], 
                    sample_rate: int = AUDIO_CONFIG["sample_rate"]) -> str:
        """
        Record audio from microphone
        
        Args:
            duration: Duration in seconds
            sample_rate: Sample rate in Hz
            
        Returns:
            Path to saved audio file
        """
        print(f"\n🎤 Recording for {duration} seconds... Speak now!")
        
        try:
            # Record audio
            audio_data = sd.rec(
                int(duration * sample_rate),
                samplerate=sample_rate,
                channels=AUDIO_CONFIG["channels"],
                dtype='float32'
            )
            sd.wait()  # Wait for recording to finish
            print("✓ Recording complete")
            
            # Save audio to file
            filename = os.path.join(self.audio_dir, f"recording_{np.random.randint(1000, 9999)}.wav")
            sf.write(filename, audio_data, sample_rate)
            
            return filename
        
        except Exception as e:
            print(f"❌ Error recording audio: {e}")
            raise
    
    def play_audio(self, file_path: str):
        """
        Play audio file
        
        Args:
            file_path: Path to audio file
        """
        try:
            data, sample_rate = sf.read(file_path)
            print(f"\n🔊 Playing audio...")
            sd.play(data, sample_rate)
            sd.wait()
            print("✓ Playback complete")
        
        except Exception as e:
            print(f"❌ Error playing audio: {e}")
            raise
    
    def cleanup_audio_files(self):
        """Remove temporary audio files"""
        try:
            if os.path.exists(self.audio_dir):
                for filename in os.listdir(self.audio_dir):
                    filepath = os.path.join(self.audio_dir, filename)
                    if os.path.isfile(filepath):
                        os.remove(filepath)
                print("✓ Audio files cleaned up")
        except Exception as e:
            print(f"⚠️  Warning while cleaning up: {e}")
