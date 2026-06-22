import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))

from wpipe import Pipeline
from wpipe_steps.communication import DiscordBotStep

def print_result(data):
    """Step to print Discord result."""
    status = data.get("discord_status", {})
    if status.get("success"):
        print(f"\n✅ Discord Message Sent!")
        print(f"Status Code: {status['status_code']}")
    else:
        print(f"\n❌ Discord Failed: {status.get('error')}")
    return data

def main():
    pipeline = Pipeline(pipeline_name="Discord_Demo", verbose=True)

    # Replace with your actual Discord webhook URL
    send_discord = DiscordBotStep.as_step(
        name="Send_Discord",
        webhook_url="https://discord.com/api/webhooks/YOUR/WEBHOOK",
        message="🚀 Pipeline completed successfully!"
    )

    pipeline.set_steps([
        send_discord,
        print_result
    ])

    print("🚀 Starting Discord Bot Demo Pipeline...")
    pipeline.run({})

if __name__ == "__main__":
    main()
