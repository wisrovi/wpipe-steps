"""
Example: HFAudioEmotionRecognitionStep
Recognize emotions in audio.
"""
from wpipe import Pipeline
from wpipe_steps.huggingface import HFAudioEmotionRecognitionStep

def main():
    pipeline = Pipeline(pipeline_name="audio_emotion_example")
    pipeline.set_steps([
        HFAudioEmotionRecognitionStep.as_step(
            name="detect_emotion",
            model_name="ehcalabres/wav2vec2-lg-xlsr-en-speech-emotion-recognition",
            response_key="emotion"
        )
    ])
    result = pipeline.run({"audio_path": "path/to/audio.wav"})
    print("Detected Emotion:", result.get("emotion"))

if __name__ == "__main__":
    main()
