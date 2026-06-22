"""
Example: HFSpeakerDiarizationStep
Identify speakers in audio (who spoke when).
"""
from wpipe import Pipeline
from wpipe_steps.ai import HFSpeakerDiarizationStep

def main():
    pipeline = Pipeline(pipeline_name="diarization_example")
    pipeline.set_steps([
        HFSpeakerDiarizationStep.as_step(
            name="diarize_speakers",
            model_name="pyannote/speaker-diarization",
            response_key="speaker_segments"
        )
    ])
    result = pipeline.run({"audio_path": "path/to/conversation.wav"})
    print("Speaker Segments:", result.get("speaker_segments"))

if __name__ == "__main__":
    main()
