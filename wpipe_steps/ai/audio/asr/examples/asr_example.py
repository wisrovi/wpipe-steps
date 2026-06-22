"""
Example: HFAutomaticSpeechRecognitionStep
Transcribe speech from audio to text.
"""
from wpipe import Pipeline
from wpipe_steps.ai import HFAutomaticSpeechRecognitionStep

def main():
    pipeline = Pipeline(pipeline_name="asr_example")
    pipeline.set_steps([
        HFAutomaticSpeechRecognitionStep.as_step(
            name="transcribe_audio",
            model_name="openai/whisper-tiny",
            response_key="transcription"
        )
    ])
    result = pipeline.run({"audio_path": "path/to/audio.wav"})
    print("Transcription:", result.get("transcription"))

if __name__ == "__main__":
    main()
