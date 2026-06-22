"""
Example: HFVideoClassificationStep
Classify video content.
"""
from wpipe import Pipeline
from wpipe_steps.ai import HFVideoClassificationStep

def main():
    pipeline = Pipeline(pipeline_name="video_classification_example")
    pipeline.set_steps([
        HFVideoClassificationStep.as_step(
            name="classify_video",
            model_name="MCG-NJU/videomae-base-finetuned-kinetics",
            top_k=3,
            response_key="video_class"
        )
    ])
    result = pipeline.run({"video_path": "path/to/video.mp4"})
    print("Video Classification:", result.get("video_class"))

if __name__ == "__main__":
    main()
