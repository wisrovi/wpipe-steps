"""
Example: HFImageColorizationStep
Colorize black and white images.
"""
from wpipe import Pipeline
from wpipe_steps.ai import HFImageColorizationStep

def main():
    pipeline = Pipeline(pipeline_name="colorization_example")
    pipeline.set_steps([
        HFImageColorizationStep.as_step(
            name="colorize_image",
            model_name="piddnad/DDColor",
            response_key="colorized_image"
        )
    ])
    result = pipeline.run({"image_path": "path/to/bw_image.jpg"})
    print("Colorized Image saved to:", result.get("colorized_image"))

if __name__ == "__main__":
    main()
