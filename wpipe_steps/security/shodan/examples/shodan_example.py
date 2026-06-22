import sys
from pathlib import Path

# Add project root to path for local development testing
sys.path.append(str(Path(__file__).parent.parent.parent))

from wpipe import Pipeline
from wpipe_steps.security import ShodanSearchStep

def main():
    pipeline = Pipeline(pipeline_name="Shodan_Security_Demo", verbose=True)

    # Example: Search for an IP on Shodan
    shodan_step = ShodanSearchStep.as_step(
        name="Search_IP_Shodan",
        api_key="YOUR_SHODAN_API_KEY", # Replace with real key
        query="8.8.8.8",
        search_type="host"
    )

    pipeline.set_steps([
        shodan_step,
        lambda d: print(f"\n🌍 Shodan Data for {d['shodan_results']['query']}: {d['shodan_results']['data'].get('org')}") or d
    ])

    print("🚀 Shodan Step defined. (Execution requires real API Key)")

if __name__ == "__main__":
    main()
