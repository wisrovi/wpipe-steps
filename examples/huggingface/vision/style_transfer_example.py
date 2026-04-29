"""
Example: HFImageStyleTransferStep
Apply artistic style to images.
"""
from wpipe import Pipeline
from wpipe_steps.huggingface import HFImageStyleTransferStep

def main():
    pipeline = Pipeline(pipeline_name="style_transfer_example")
    pipeline.set_steps([
        HFImageStyleTransferStep.as_step(
            name="apply_style",
            model_name="timbrooks/instruct-pix2pix",
            style_prompt="in the style of Van Gogh",
            response_key="styled_image"
        )
    ])
    result = pipeline.run({"image_path": "path/to/image.jpg"})
    print("Styled Image saved to:", result.get("styled_image"))

if __name__ == "__main__":
    main()
