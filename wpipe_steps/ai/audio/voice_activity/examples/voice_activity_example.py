"""
Example: HFVoiceActivityDetectionStep
Detect voice activity in audio.
"""
from wpipe import Pipeline
from wpipe_steps.ai import HFVoiceActivityDetectionStep

def main():
    pipeline = Pipeline(pipeline_name="vad_example")
    pipeline.set_steps([
        HFVoiceActivityDetectionStep.as_step(
            name="detect_voice",
            model_name="speechbrain/voice-activity-detection",
            response_key="voice_segments"
        )
    ])
    result = pipeline.run({"audio_path": "path/to/audio.wav"})
    print("Voice Segments:", result.get("voice_segments"))

if __name__ == "__main__":
    main()
