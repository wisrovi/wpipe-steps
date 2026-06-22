"""
Example: HFSpeechToSpeechStep
Convert speech from one voice to another.
"""
from wpipe import Pipeline
from wpipe_steps.ai import HFSpeechToSpeechStep

def main():
    pipeline = Pipeline(pipeline_name="speech_conversion_example")
    pipeline.set_steps([
        HFSpeechToSpeechStep.as_step(
            name="convert_speech",
            model_name="matanyadaev/voice-conversion",
            response_key="converted_audio"
        )
    ])
    result = pipeline.run({"audio_path": "path/to/source_audio.wav"})
    print("Converted Audio saved to:", result.get("converted_audio"))

if __name__ == "__main__":
    main()
