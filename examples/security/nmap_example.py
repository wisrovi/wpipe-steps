import sys
from pathlib import Path

# Add project root to path for local development testing
sys.path.append(str(Path(__file__).parent.parent.parent))

from wpipe import Pipeline
from wpipe_steps.security import NmapScanStep

def main():
    pipeline = Pipeline(pipeline_name="Nmap_Security_Demo", verbose=True)

    # Example: Scan localhost for common ports
    scan_step = NmapScanStep.as_step(
        name="Local_Port_Scan",
        target="127.0.0.1",
        ports="80,443,3306"
    )

    pipeline.set_steps([
        scan_step,
        lambda d: print(f"\n🔍 Nmap Results for {d['nmap_scan']['target']}: {d['nmap_scan']['results']}") or d
    ])

    print("🚀 Nmap Step defined. (Execution requires nmap installed)")
    # Run
    # pipeline.run({})

if __name__ == "__main__":
    main()
