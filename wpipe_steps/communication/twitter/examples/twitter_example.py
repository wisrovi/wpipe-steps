import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))

from wpipe import Pipeline
from wpipe_steps.communication import TwitterPostStep

def print_result(data):
    """Step to print Twitter result."""
    status = data.get("twitter_status", {})
    if status.get("success"):
        print(f"\n✅ Tweet Posted!")
        print(f"Message: {status['message']}")
    else:
        print(f"\n❌ Twitter Failed: {status.get('error')}")
    return data

def main():
    pipeline = Pipeline(pipeline_name="Twitter_Demo", verbose=True)

    # Replace with your actual Twitter bearer token
    post_tweet = TwitterPostStep.as_step(
        name="Post_Tweet",
        bearer_token="YOUR_TWITTER_BEARER_TOKEN",
        message="🚀 Pipeline completed successfully! #automation #wpipe"
    )

    pipeline.set_steps([
        post_tweet,
        print_result
    ])

    print("🚀 Starting Twitter Post Demo Pipeline...")
    pipeline.run({})

if __name__ == "__main__":
    main()
