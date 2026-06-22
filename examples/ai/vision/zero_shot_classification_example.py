"""
Example: HFZeroShotImageClassificationStep
Classify images into custom categories without training.
"""
from wpipe import Pipeline
from wpipe_steps.ai import HFZeroShotImageClassificationStep

def main():
    pipeline = Pipeline(pipeline_name="zero_shot_image_example")
    pipeline.set_steps([
        HFZeroShotImageClassificationStep.as_step(
            name="classify_zero_shot_image",
            model_name="openai/clip-vit-base-patch32",
            candidate_labels=["cat", "dog", "car", "tree"],
            response_key="zero_shot_image_class"
        )
    ])
    result = pipeline.run({"image_path": "path/to/image.jpg"})
    print("Zero-Shot Image Classification:", result.get("zero_shot_image_class"))

if __name__ == "__main__":
    main()
