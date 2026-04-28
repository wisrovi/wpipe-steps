import sys
from pathlib import Path

# Add project root to path for local development testing
sys.path.append(str(Path(__file__).parent.parent.parent))

from wpipe import Pipeline
from wpipe_steps.security import Fail2BanCheckStep

def print_result(data):
    """Step to print the Fail2Ban check result."""
    status = data.get("fail2ban_status", {})
    if status.get("success"):
        print(f"\n✅ Check Complete!")
        print(f"IP: {status['ip']}")
        print(f"Banned: {status['is_banned']}")
    else:
        print(f"\n❌ Check Failed: {status.get('error')}")
    return data

def main():
    # 1. Create the pipeline
    pipeline = Pipeline(pipeline_name="Fail2Ban_Check_Demo", verbose=True)

    # 2. Define steps
    check_ip = Fail2BanCheckStep.as_step(
        name="Check_Banned_IP",
        ip_to_check="192.168.1.100",
        log_path="/var/log/fail2ban.log"
    )

    pipeline.set_steps([
        check_ip,
        print_result
    ])

    # 3. Run
    print("🚀 Starting Fail2Ban Check Demo Pipeline...")
    pipeline.run({})

if __name__ == "__main__":
    main()
