"""
Example: HFInpaintingStep
Fill in missing parts of images (inpainting).
"""
from wpipe import Pipeline
from wpipe_steps.ai import HFInpaintingStep

def main():
    pipeline = Pipeline(pipeline_name="inpainting_example")
    pipeline.set_steps([
        HFInpaintingStep.as_step(
            name="inpaint_image",
            model_name="runwayml/stable-diffusion-inpainting",
            prompt="a beautiful landscape",
            mask_path="path/to/mask.png",
            response_key="inpainted_image"
        )
    ])
    result = pipeline.run({"image_path": "path/to/image.jpg"})
    print("Inpainted Image saved to:", result.get("inpainted_image"))

if __name__ == "__main__":
    main()
