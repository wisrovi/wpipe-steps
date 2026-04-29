import sys
from pathlib import Path

# Add project root to path for local development testing
sys.path.append(str(Path(__file__).parent.parent.parent))

from wpipe import Pipeline
from wpipe_steps.communication import TelegramNotifyStep

def main():
    pipeline = Pipeline(pipeline_name="Telegram_Communication_Demo", verbose=True)

    # Example: Send a critical alert
    tg_step = TelegramNotifyStep.as_step(
        name="Critical_Alert",
        bot_token="YOUR_BOT_TOKEN",
        chat_id="YOUR_CHAT_ID",
        message="🚨 <b>Pipeline Alert:</b> Task failed successfully!"
    )

    pipeline.set_steps([
        tg_step,
        lambda d: print(f"\n📢 Telegram Success: {d['telegram_status']['success']}") or d
    ])

    print("🚀 Telegram Step defined. (Execution requires Bot Token)")

if __name__ == "__main__":
    main()
