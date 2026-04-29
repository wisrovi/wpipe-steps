"""
Example: HFImageToImageStep
Transform images (style transfer, enhancement, etc.).
"""
from wpipe import Pipeline
from wpipe_steps.huggingface import HFImageToImageStep

def main():
    pipeline = Pipeline(pipeline_name="image2image_example")
    pipeline.set_steps([
        HFImageToImageStep.as_step(
            name="transform_image",
            model_name="timbrooks/instruct-pix2pix",
            prompt="turn the image into a painting",
            response_key="transformed_image"
        )
    ])
    result = pipeline.run({"image_path": "path/to/image.jpg"})
    print("Transformed Image saved to:", result.get("transformed_image"))

if __name__ == "__main__":
    main()
