import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))

from wpipe import Pipeline
from wpipe_steps.multimedia import TtsGenerateStep

def print_result(data):
    """Step to print TTS result."""
    status = data.get("tts_status", {})
    if status.get("success"):
        print(f"\n✅ Text-to-Speech Generated!")
        print(f"Output: {status['output']}")
        print(f"Language: {status['language']}")
    else:
        print(f"\n❌ TTS Failed: {status.get('error')}")
    return data

def main():
    pipeline = Pipeline(pipeline_name="TTS_Demo", verbose=True)

    generate = TtsGenerateStep.as_step(
        name="Generate_Speech",
        text="Hello, this is a test of text to speech synthesis.",
        language="en",
        output_path="output.mp3"
    )

    pipeline.set_steps([
        generate,
        print_result
    ])

    print("🚀 Starting TTS Generate Demo Pipeline...")
    pipeline.run({})

if __name__ == "__main__":
    main()
