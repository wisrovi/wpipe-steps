import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))

from wpipe import Pipeline
from wpipe_steps.communication import TelegramNotifyStep

def print_result(data):
    """Step to print Telegram result."""
    status = data.get("telegram_status", {})
    if status.get("success"):
        print(f"\n✅ Telegram Sent!")
        print(f"Message: {status['message_sent']}")
    else:
        print(f"\n❌ Telegram Failed: {status.get('error')}")
    return data

def main():
    pipeline = Pipeline(pipeline_name="Telegram_Demo", verbose=True)

    # Replace with your actual bot token and chat_id
    notify = TelegramNotifyStep.as_step(
        name="Send_Telegram",
        bot_token="YOUR_BOT_TOKEN",
        chat_id="YOUR_CHAT_ID",
        message="🚀 Pipeline completed successfully!"
    )

    pipeline.set_steps([
        notify,
        print_result
    ])

    print("🚀 Starting Telegram Demo Pipeline...")
    pipeline.run({})

if __name__ == "__main__":
    main()
