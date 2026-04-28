import sys
from pathlib import Path

# Add project root to path for local development testing
sys.path.append(str(Path(__file__).parent.parent.parent))

from wpipe import Pipeline
from wpipe_steps.security import Fail2BanCheckStep

def main():
    pipeline = Pipeline(pipeline_name="Security_Audit_Demo", verbose=True)

    # Example: Check if a suspicious IP is banned
    check_ip = Fail2BanCheckStep.as_step(
        name="Check_Attacker_IP",
        ip_to_check="192.168.1.100",
        log_path="tests/mock_fail2ban.log" # Use mock log for demo
    )

    pipeline.set_steps([
        check_ip,
        lambda d: print(f"\n🛡️ IP Banned: {d['fail2ban_status']['is_banned']}") or d
    ])

    print("🚀 Fail2Ban Step defined.")
    # Run with default empty dict
    pipeline.run({})

if __name__ == "__main__":
    main()
