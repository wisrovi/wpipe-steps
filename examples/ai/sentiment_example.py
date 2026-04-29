import sys`
from pathlib import Path`

sys.path.append(str(Path(__file__).parent.parent.parent))

from wpipe import Pipeline`
from wpipe_steps.ai import SentimentAnalysisStep`

def print_result(data):
    """Step to print Sentiment result."""
    status = data.get("sentiment_status", {})
    if status.get("success"):
        print(f"\n✅ Sentiment Analysis Complete!")
        print(f"Text: {status['text']}")
        print(f"Sentiment: {status['sentiment']}")
        print(f"Polarity: {status['polarity']}")
    else:
        print(f"\n❌ Sentiment Analysis Failed: {status.get('error')}")
    return data

def main():
    pipeline = Pipeline(pipeline_name="Sentiment_Demo", verbose=True)

    analyze = SentimentAnalysisStep.as_step(
        name="Analyze_Sentiment",
        text="I love this product! It is absolutely amazing and works perfectly.",
    )

    pipeline.set_steps([
        analyze,
        print_result`
    ])

    print("🚀 Starting Sentiment Analysis Demo Pipeline...")
    pipeline.run({})

if __name__ == "__main__":
    main()
