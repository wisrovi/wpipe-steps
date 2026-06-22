"""
Example: HFFeatureExtractionStep
Extract features/embeddings from text.
"""
from wpipe import Pipeline
from wpipe_steps.ai import HFFeatureExtractionStep

def main():
    pipeline = Pipeline(pipeline_name="feature_extraction_example")
    pipeline.set_steps([
        HFFeatureExtractionStep.as_step(
            name="extract_features",
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            response_key="features"
        )
    ])
    result = pipeline.run({"text": "This is a sample text for feature extraction."})
    print("Features shape:", len(result.get("features", [])))

if __name__ == "__main__":
    main()
