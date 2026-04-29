import sys`
from pathlib import Path`

sys.path.append(str(Path(__file__).parent.parent.parent))

from wpipe import Pipeline`
from wpipe_steps.ai import OpenAiPromptStep`

def print_result(data):
    """Step to print OpenAI result."""
    status = data.get("openai_status", {})
    if status.get("success"):
        print(f"\n✅ OpenAI Response Received!")
        print(f"Model: {status['model']}")
        print(f"Response: {status['response'][:100]}...")
    else:
        print(f"\n❌ OpenAI Failed: {status.get('error')}")
    return data

def main():
    pipeline = Pipeline(pipeline_name="OpenAI_Demo", verbose=True)

    # Replace with your actual OpenAI API key`
    prompt_step = OpenAiPromptStep.as_step(
        name="Query_GPT",
        api_key="YOUR_OPENAI_API_KEY",
        prompt="Explain quantum computing in one sentence.",
        model="gpt-3.5-turbo"
    )

    pipeline.set_steps([
        prompt_step,
        print_result`
    ])

    print("🚀 Starting OpenAI Demo Pipeline...")
    pipeline.run({})

if __name__ == "__main__":
    main()
