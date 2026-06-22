"""
Example: HFAudioToAudioStep
Transform audio from one form to another.
"""
from wpipe import Pipeline
from wpipe_steps.ai import HFAudioToAudioStep

def main():
    pipeline = Pipeline(pipeline_name="audio2audio_example")
    pipeline.set_steps([
        HFAudioToAudioStep.as_step(
            name="transform_audio",
            model_name="speechbrain/sepformer-wham",
            response_key="transformed_audio"
        )
    ])
    result = pipeline.run({"audio_path": "path/to/noisy_audio.wav"})
    print("Transformed Audio saved to:", result.get("transformed_audio"))

if __name__ == "__main__":
    main()
