"""
Example: HFImageTextToTextStep
Multimodal image+text to text generation.
"""
from wpipe import Pipeline
from wpipe_steps.huggingface import HFImageTextToTextStep

def main():
    pipeline = Pipeline(pipeline_name="image_text_example")
    pipeline.set_steps([
        HFImageTextToTextStep.as_step(
            name="process_image_text",
            model_name="llava-hf/llava-1.5-7b-hf",
            response_key="response"
        )
    ])
    result = pipeline.run({
        "image_path": "path/to/image.jpg",
        "text": "Describe this image in detail."
    })
    print("Response:", result.get("response"))

if __name__ == "__main__":
    main()
