"""
Example: HFTextClassificationStep
Classify text sentiment using local HuggingFace model.
"""
from wpipe import Pipeline
from wpipe_steps.ai import HFTextClassificationStep

def main():
    pipeline = Pipeline(pipeline_name="text_classification_example")
    pipeline.set_steps([
        HFTextClassificationStep.as_step(
            name="classify_text",
            model_name="distilbert-base-uncased-finetuned-sst-2-english",
            top_k=3,
            response_key="classification_result"
        )
    ])
    result = pipeline.run({"text": "I love this product! It works amazingly well."})
    print("Classification Result:", result.get("classification_result"))

if __name__ == "__main__":
    main()
