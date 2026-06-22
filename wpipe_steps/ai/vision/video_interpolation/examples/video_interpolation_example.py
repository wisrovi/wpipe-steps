"""
Example: HFVideoFrameInterpolationStep
Generate intermediate frames in video (slow motion).
"""
from wpipe import Pipeline
from wpipe_steps.ai import HFVideoFrameInterpolationStep

def main():
    pipeline = Pipeline(pipeline_name="video_interpolation_example")
    pipeline.set_steps([
        HFVideoFrameInterpolationStep.as_step(
            name="interpolate_frames",
            model_name="zhucunxiao/Video-Frame-Interpolation",
            response_key="interpolated_video"
        )
    ])
    result = pipeline.run({"video_path": "path/to/video.mp4"})
    print("Interpolated Video saved to:", result.get("interpolated_video"))

if __name__ == "__main__":
    main()
