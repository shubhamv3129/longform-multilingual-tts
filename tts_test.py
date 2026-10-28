"""
Backwards-compatible entry point for long-form TTS generation.
"""
from feature_long_audio_tts import generate_audio, get_10_min_script, smart_split_text

__all__ = ["generate_audio", "get_10_min_script", "smart_split_text"]

if __name__ == "__main__":
    generate_audio()
