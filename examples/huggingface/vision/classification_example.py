"""
Example: HFImageClassificationStep
Classify images into categories.
"""
from wpipe import Pipeline
from wpipe_steps.huggingface import HFImageClassificationStep

def main():
    pipeline = Pipeline(pipeline_name="image_classification_example")
    pipeline.set_steps([
        HFImageClassificationStep.as_step(
            name="classify_image",
            model_name="google/vit-base-patch16-224",
            top_k=3,
            response_key="image_class"
        )
    ])
    result = pipeline.run({"image_path": "path/to/image.jpg"})
    print("Image Classification:", result.get("image_class"))

if __name__ == "__main__":
    main()
