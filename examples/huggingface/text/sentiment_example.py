"""
Example: HFSentimentAnalysisStep
Analyze sentiment of text using local HuggingFace model.
"""
from wpipe import Pipeline
from wpipe_steps.huggingface import HFSentimentAnalysisStep

def main():
    pipeline = Pipeline(pipeline_name="sentiment_example")
    pipeline.set_steps([
        HFSentimentAnalysisStep.as_step(
            name="analyze_sentiment",
            model_name="distilbert-base-uncased-finetuned-sst-2-english",
            response_key="sentiment_result"
        )
    ])
    result = pipeline.run({"text": "This product is absolutely terrible and disappointing."})
    print("Sentiment Result:", result.get("sentiment_result"))

if __name__ == "__main__":
    main()
