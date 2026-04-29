"""
Example: HFAudioClassificationStep
Classify audio content.
"""
from wpipe import Pipeline
from wpipe_steps.huggingface import HFAudioClassificationStep

def main():
    pipeline = Pipeline(pipeline_name="audio_classification_example")
    pipeline.set_steps([
        HFAudioClassificationStep.as_step(
            name="classify_audio",
            model_name="superb/wav2vec2-base-superb-ks",
            top_k=3,
            response_key="audio_class"
        )
    ])
    result = pipeline.run({"audio_path": "path/to/audio.wav"})
    print("Audio Classification:", result.get("audio_class"))

if __name__ == "__main__":
    main()
