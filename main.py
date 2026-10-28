"""
Main entry point for the Long-Form Multilingual Neural TTS suite.
Showcases both English long-form documentary synthesis (Journey-D) and
Hindi narrative storytelling synthesis (gemini-2.5-pro-tts / Algenib).
"""
import argparse
from feature_long_audio_tts import generate_audio
from feature_story_gen import generate_gemini_audio


def example_english_documentary_tts() -> None:
    """
    Synthesizes the 10-minute English documentary script ('The Silent Pulse')
    using sentence-boundary chunking and binary MP3 stream concatenation.
    """
    generate_audio()


def example_hindi_story_tts() -> None:
    """
    Synthesizes the Hindi narrative story using the `gemini-2.5-pro-tts` model.
    """
    generate_gemini_audio()


def main() -> None:
    """
    CLI entry point supporting `--mode english`, `--mode hindi`, or `--mode all`.
    """
    parser = argparse.ArgumentParser(
        description="Long-Form Multilingual Neural TTS Generator"
    )
    parser.add_argument(
        "--mode",
        choices=["english", "hindi", "all"],
        default="all",
        help="Select which synthesis pipeline to execute (default: all).",
    )
    args = parser.parse_args()

    if args.mode in ("english", "all"):
        print("=== Running English Long-Form Documentary Synthesis ===")
        example_english_documentary_tts()

    if args.mode in ("hindi", "all"):
        print("\n=== Running Hindi Story Synthesis (gemini-2.5-pro-tts) ===")
        example_hindi_story_tts()


if __name__ == "__main__":
    main()
