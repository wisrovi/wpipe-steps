"""
Example: HFFillMaskStep
Fill in the blank (masked token) in text.
"""
from wpipe import Pipeline
from wpipe_steps.ai import HFFillMaskStep

def main():
    pipeline = Pipeline(pipeline_name="fill_mask_example")
    pipeline.set_steps([
        HFFillMaskStep.as_step(
            name="fill_mask",
            model_name="bert-base-uncased",
            top_k=3,
            response_key="mask_predictions"
        )
    ])
    result = pipeline.run({"text": "The capital of France is [MASK]."})
    print("Mask Predictions:", result.get("mask_predictions"))

if __name__ == "__main__":
    main()
