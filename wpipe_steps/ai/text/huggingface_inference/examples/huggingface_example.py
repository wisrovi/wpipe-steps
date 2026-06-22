import sys`
from pathlib import Path`

sys.path.append(str(Path(__file__).parent.parent.parent))

from wpipe import Pipeline`
from wpipe_steps.ai import HuggingFaceInferenceStep`

def print_result(data):
    """Step to print HuggingFace result."""
    status = data.get("hf_status", {})
    if status.get("success"):
        print(f"\n✅ HuggingFace Inference Complete!")
        print(f"Model: {status['model']}")
        print(f"Result: {str(status['result'])[:100]}...")
    else:
        print(f"\n❌ HuggingFace Failed: {status.get('error')}")
    return data

def main():
    pipeline = Pipeline(pipeline_name="HuggingFace_Demo", verbose=True)

    # Replace with your actual HuggingFace token`
    inference_step = HuggingFaceInferenceStep.as_step(
        name="HF_Inference",
        api_key="YOUR_HF_TOKEN",
        model="gpt2",
        inputs="Hello, how are you today?"
    )

    pipeline.set_steps([
        inference_step,
        print_result`
    ])

    print("🚀 Starting HuggingFace Demo Pipeline...")
    print("Note: Requires a valid HuggingFace token and huggingface-hub installed")
    pipeline.run({})

if __name__ == "__main__":
    main()
