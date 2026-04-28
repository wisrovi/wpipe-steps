import sys
from pathlib import Path

# Add project root to path for local development testing
sys.path.append(str(Path(__file__).parent.parent.parent))

from wpipe import Pipeline
from wpipe_steps.connectivity import HttpRequestStep

def print_result(data):
    """Step to print the HTTP response info."""
    resp = data.get("user_data", {})
    if resp.get("success"):
        print(f"\n✅ Request Successful!")
        print(f"Status Code: {resp['status_code']}")
        print(f"Data: {resp['content']}")
    else:
        print(f"\n❌ Request Failed: {resp.get('error')}")
    return data

def main():
    # 1. Create the pipeline
    pipeline = Pipeline(pipeline_name="HTTP_Connectivity_Demo", verbose=True)

    # 2. Define steps
    # We use a public test API (JSONPlaceholder)
    fetch_user = HttpRequestStep.as_step(
        name="Get_Public_User",
        url="https://jsonplaceholder.typicode.com/users/1",
        method="GET",
        response_key="user_data"
    )

    pipeline.set_steps([
        fetch_user,
        print_result
    ])

    # 3. Run
    print("🚀 Starting HTTP Demo Pipeline...")
    pipeline.run({})

if __name__ == "__main__":
    main()
