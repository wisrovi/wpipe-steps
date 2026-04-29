import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))

from wpipe import Pipeline
from wpipe_steps.communication import SlackAlertStep

def print_result(data):
    """Step to print Slack result."""
    status = data.get("slack_status", {})
    if status.get("success"):
        print(f"\n✅ Slack Alert Sent!")
        print(f"Status Code: {status['status_code']}")
    else:
        print(f"\n❌ Slack Failed: {status.get('error')}")
    return data

def main():
    pipeline = Pipeline(pipeline_name="Slack_Demo", verbose=True)

    # Replace with your actual Slack webhook URL
    send_alert = SlackAlertStep.as_step(
        name="Notify_Slack",
        webhook_url="https://hooks.slack.com/services/YOUR/WEBHOOK/URL",
        message="🚀 Pipeline completed successfully!",
        channel="#general"
    )

    pipeline.set_steps([
        send_alert,
        print_result
    ])

    print("🚀 Starting Slack Alert Demo Pipeline...")
    pipeline.run({})

if __name__ == "__main__":
    main()
