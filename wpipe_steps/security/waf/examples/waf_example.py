import sys
from pathlib import Path

# Add project root to path for local development testing
sys.path.append(str(Path(__file__).parent.parent.parent))

from wpipe import Pipeline
from wpipe_steps.security import WafFilterStep

def print_result(data):
    """Step to print the WAF filter result."""
    status = data.get("waf_status", {})
    print(f"\n🛡️ WAF Filter Results:")
    print(f"Threats detected: {status['threats_count']}")
    if status['threats_count'] > 0:
        for threat in status['threats']:
            print(f"  - Key: {threat['key']}, Type: {threat['type']}")
    else:
        print("  No threats detected!")
    return data

def main():
    # 1. Create the pipeline
    pipeline = Pipeline(pipeline_name="WAF_Filter_Demo", verbose=True)

    # 2. Define steps
    filter_input = WafFilterStep.as_step(
        name="Filter_User_Input",
        keys_to_filter=["user_input", "query_params"],
        strict_mode=False
    )

    pipeline.set_steps([
        filter_input,
        print_result
    ])

    # 3. Run with sample data (including malicious content)
    print("🚀 Starting WAF Filter Demo Pipeline...")
    pipeline.run({
        "user_input": "Hello World",
        "query_params": "1' OR '1'='1"  # SQL injection attempt
    })

if __name__ == "__main__":
    main()
