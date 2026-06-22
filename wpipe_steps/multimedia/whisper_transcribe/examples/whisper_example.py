import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))

from wpipe import Pipeline
from wpipe_steps.multimedia import WhisperTranscribeStep

def print_result(data):
    """Step to print Whisper result."""
    status = data.get("whisper_status", {})
    if status.get("success"):
        print(f"\n✅ Audio Transcribed!")
        print(f"Language: {status['language']}")
        print(f"Text: {status['text'][:100]}...")  # Show first 100 chars
    else:
        print(f"\n❌ Transcription Failed: {status.get('error')}")
    return data

def main():
    pipeline = Pipeline(pipeline_name="Whisper_Demo", verbose=True)

    transcribe = WhisperTranscribeStep.as_step(
        name="Transcribe_Audio",
        audio_path="test_audio.mp3",
        model_size="base"
    )

    pipeline.set_steps([
        transcribe,
        print_result
    ])

    print("🚀 Starting Whisper Transcription Demo Pipeline...")
    print("Note: Requires a valid audio file and openai-whisper installed")
    pipeline.run({})

if __name__ == "__main__":
    main()
