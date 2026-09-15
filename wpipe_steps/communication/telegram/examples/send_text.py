from wpipe import Pipeline
from wpipe_steps.communication import TelegramSendTextStep


def print_result(data):
    """Step to print Telegram text result."""
    status = data.get("telegram_status", {})
    if status.get("success"):
        print(f"✅ Telegram Text Sent: {status.get('message_sent')}")
    else:
        print(f"❌ Telegram Text Failed: {status.get('error')}")
    return data


def main():
    pipeline = Pipeline(pipeline_name="Telegram_Send_Text_Demo", verbose=True)

    pipeline.set_steps(
        [
            TelegramSendTextStep(
                name="Send_Telegram_Text",
                bot_token="YOUR_BOT_TOKEN",
            ),
            print_result,
        ]
    )

    print("🚀 Running Telegram Send Text Pipeline...")
    pipeline.run(
        {
            "telegram": {
                "type": "text",
                "message": "Hello from the Telegram text pipeline example!",
                "chat_id": "YOUR_CHAT_ID",
            }
        }
    )


if __name__ == "__main__":
    main()
