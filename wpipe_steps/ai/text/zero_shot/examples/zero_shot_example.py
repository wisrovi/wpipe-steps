"""
Example: HFZeroShotClassificationStep
Classify text into custom labels without training.
"""
from wpipe import Pipeline
from wpipe_steps.ai import HFZeroShotClassificationStep

def main():
    pipeline = Pipeline(pipeline_name="zero_shot_example")
    pipeline.set_steps([
        HFZeroShotClassificationStep.as_step(
            name="classify_zero_shot",
            model_name="facebook/bart-large-mnli",
            candidate_labels=["technology", "sports", "politics", "entertainment"],
            response_key="zero_shot_result"
        )
    ])
    result = pipeline.run({"text": "Apple released a new iPhone with amazing features."})
    print("Zero-Shot Classification:", result.get("zero_shot_result"))

if __name__ == "__main__":
    main()
