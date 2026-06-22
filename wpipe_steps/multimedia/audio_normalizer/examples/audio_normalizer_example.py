import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))

from wpipe import Pipeline
from wpipe_steps.multimedia import AudioNormalizerStep

def print_result(data):
    """Step to print Audio Normalizer result."""
    status = data.get("audio_status", {})
    if status.get("success"):
        print(f"\n✅ Audio Normalized!")
        print(f"Output: {status['output']}")
        print(f"Duration: {status['duration']}s")
    else:
        print(f"\n❌ Normalization Failed: {status.get('error')}")
    return data

def main():
    pipeline = Pipeline(pipeline_name="Audio_Normalizer_Demo", verbose=True)

    normalize = AudioNormalizerStep.as_step(
        name="Normalize_Audio",
        input_path="test_audio.wav"
    )

    pipeline.set_steps([
        normalize,
        print_result
    ])

    print("🚀 Starting Audio Normalizer Demo Pipeline...")
    print("Note: Requires a valid .wav file to test")
    pipeline.run({})

if __name__ == "__main__":
    main()
