"""
Example: HFImageBackgroundRemovalStep
Remove background from images.
"""
from wpipe import Pipeline
from wpipe_steps.ai import HFImageBackgroundRemovalStep

def main():
    pipeline = Pipeline(pipeline_name="background_removal_example")
    pipeline.set_steps([
        HFImageBackgroundRemovalStep.as_step(
            name="remove_background",
            model_name="briaai/RMBG-1.4",
            response_key="foreground_image"
        )
    ])
    result = pipeline.run({"image_path": "path/to/image_with_bg.jpg"})
    print("Foreground Image saved to:", result.get("foreground_image"))

if __name__ == "__main__":
    main()
