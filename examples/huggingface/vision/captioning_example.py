"""
Example: HFImageToTextStep (Image Captioning)
Generate text descriptions of images.
"""
from wpipe import Pipeline
from wpipe_steps.huggingface import HFImageToTextStep

def main():
    pipeline = Pipeline(pipeline_name="captioning_example")
    pipeline.set_steps([
        HFImageToTextStep.as_step(
            name="caption_image",
            model_name="nlpconnect/vit-gpt2-image-captioning",
            response_key="caption"
        )
    ])
    result = pipeline.run({"image_path": "path/to/image.jpg"})
    print("Image Caption:", result.get("caption"))

if __name__ == "__main__":
    main()
