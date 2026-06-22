"""
Example: HFDepthEstimationStep
Estimate depth in images (3D from 2D).
"""
from wpipe import Pipeline
from wpipe_steps.ai import HFDepthEstimationStep

def main():
    pipeline = Pipeline(pipeline_name="depth_estimation_example")
    pipeline.set_steps([
        HFDepthEstimationStep.as_step(
            name="estimate_depth",
            model_name="Intel/dpt-large",
            response_key="depth_map"
        )
    ])
    result = pipeline.run({"image_path": "path/to/image.jpg"})
    print("Depth Map saved to:", result.get("depth_map"))

if __name__ == "__main__":
    main()
