import sys
from pathlib import Path

# Add project root to path for local development testing
sys.path.append(str(Path(__file__).parent.parent.parent))

from wpipe import Pipeline
from wpipe_steps.infrastructure import DigitalOceanDropletStep

def main():
    pipeline = Pipeline(pipeline_name="DigitalOcean_Infrastructure_Demo", verbose=True)

    # Example: List all droplets
    do_step = DigitalOceanDropletStep.as_step(
        step_name="List_My_Droplets",
        token="YOUR_DIGITALOCEAN_TOKEN",
        operation="list"
    )

    pipeline.set_steps([
        do_step,
        lambda d: print(f"\n🌊 Droplets found: {len(d['digitalocean_status']['data'])}") or d
    ])

    print("🚀 DigitalOcean Step defined. (Execution requires DO Token)")

if __name__ == "__main__":
    main()
