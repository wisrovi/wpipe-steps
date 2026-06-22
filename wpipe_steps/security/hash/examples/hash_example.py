import sys
from pathlib import Path

# Add project root to path for local development testing
sys.path.append(str(Path(__file__).parent.parent.parent))

from wpipe import Pipeline
from wpipe_steps.security import HashGeneratorStep

def print_result(data):
    """Step to print the hash result."""
    result = data.get("hash_result", {})
    if result.get("success"):
        print(f"\n✅ Hash Generated!")
        print(f"Algorithm: {result['algorithm']}")
        print(f"Hash: {result['hash']}")
    else:
        print(f"\n❌ Hash Failed: {result.get('error')}")
    return data

def main():
    # 1. Create the pipeline
    pipeline = Pipeline(pipeline_name="Hash_Generator_Demo", verbose=True)

    # 2. Define steps
    hash_string = HashGeneratorStep.as_step(
        name="Hash_User_Password",
        algorithm="sha256",
        input_key="password"
    )

    pipeline.set_steps([
        hash_string,
        print_result
    ])

    # 3. Run with sample data
    print("🚀 Starting Hash Generator Demo Pipeline...")
    pipeline.run({"password": "mysecretpassword123"})

if __name__ == "__main__":
    main()
