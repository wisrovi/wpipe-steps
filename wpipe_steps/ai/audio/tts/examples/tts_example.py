"""
Example: HFTextToSpeechStep
Convert text to speech.
"""
from wpipe import Pipeline
from wpipe_steps.ai import HFTextToSpeechStep

def main():
    pipeline = Pipeline(pipeline_name="tts_example")
    pipeline.set_steps([
        HFTextToSpeechStep.as_step(
            name="generate_speech",
            model_name="espnet/kan-bayashi_ljspeech_vits",
            response_key="audio_output"
        )
    ])
    result = pipeline.run({"text": "Hello, this is a text to speech example."})
    print("Audio saved to:", result.get("audio_output"))

if __name__ == "__main__":
    main()
