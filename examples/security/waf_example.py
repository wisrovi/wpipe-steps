import sys
from pathlib import Path

# Add project root to path for local development testing
sys.path.append(str(Path(__file__).parent.parent.parent))

from wpipe import Pipeline
from wpipe_steps.security import WafFilterStep

def main():
    pipeline = Pipeline(pipeline_name="WAF_Security_Demo", verbose=True)

    # Example: Filter user inputs
    waf_step = WafFilterStep.as_step(
        name="WAF_Shield",
        keys_to_filter=["user_comment", "search_query"],
        strict_mode=False
    )

    pipeline.set_steps([
        waf_step,
        lambda d: print(f"\n🛡️ WAF Success: {d['waf_status']['success']} (Threats: {d['waf_status']['threats_count']})") or d
    ])

    print("🚀 Running WAF Demo Pipeline with clean input...")
    pipeline.run({"user_comment": "Hello world", "search_query": "WPipe rules"})

    print("\n🚀 Running WAF Demo Pipeline with malicious input...")
    pipeline.run({"user_comment": "<script>alert(1)</script>", "search_query": "'; DROP TABLE users; --"})

if __name__ == "__main__":
    main()
