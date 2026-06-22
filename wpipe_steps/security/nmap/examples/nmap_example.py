import sys
from pathlib import Path

# Add project root to path for local development testing
sys.path.append(str(Path(__file__).parent.parent.parent))

from wpipe import Pipeline
from wpipe_steps.security import NmapScanStep

def print_result(data):
    """Step to print the Nmap scan result."""
    scan = data.get("nmap_scan", {})
    if scan.get("success"):
        print(f"\n✅ Scan Complete!")
        print(f"Target: {scan['target']}")
        for result in scan.get("results", []):
            print(f"Host: {result['host']} - State: {result['state']}")
    else:
        print(f"\n❌ Scan Failed: {scan.get('error')}")
    return data

def main():
    # 1. Create the pipeline
    pipeline = Pipeline(pipeline_name="Nmap_Scan_Demo", verbose=True)

    # 2. Define steps
    scan_target = NmapScanStep.as_step(
        name="Scan_Target_Host",
        target="127.0.0.1",
        ports="22,80,443",
        arguments="-sV"
    )

    pipeline.set_steps([
        scan_target,
        print_result
    ])

    # 3. Run
    print("🚀 Starting Nmap Scan Demo Pipeline...")
    pipeline.run({})

if __name__ == "__main__":
    main()
