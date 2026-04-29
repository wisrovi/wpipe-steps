"""
Example: HFImageSuperResolutionStep
Upscale images (super resolution).
"""
from wpipe import Pipeline
from wpipe_steps.huggingface import HFImageSuperResolutionStep

def main():
    pipeline = Pipeline(pipeline_name="super_resolution_example")
    pipeline.set_steps([
        HFImageSuperResolutionStep.as_step(
            name="upscale_image",
            model_name="caidas/LightSR",
            response_key="upscaled_image"
        )
    ])
    result = pipeline.run({"image_path": "path/to/low_res.jpg"})
    print("Upscaled Image saved to:", result.get("upscaled_image"))

if __name__ == "__main__":
    main()
