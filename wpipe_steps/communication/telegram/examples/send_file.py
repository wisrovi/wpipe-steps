import os
from wpipe import Pipeline
from wpipe_steps.communication import TelegramSendFileStep


def print_result(data):
    """Step to print Telegram file result."""
    status = data.get("telegram_status", {})
    if status.get("success"):
        print(f"✅ Telegram File Sent: {status.get('file_sent')}")
    else:
        print(f"❌ Telegram File Failed: {status.get('error')}")
    return data


def main():
    pipeline = Pipeline(pipeline_name="Telegram_Send_File_Demo", verbose=True)

    media_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(media_dir, "media", "demo.csv")

    pipeline.set_steps(
        [
            TelegramSendFileStep(
                name="Send_Telegram_File",
                bot_token="YOUR_BOT_TOKEN",
            ),
            print_result,
        ]
    )

    print("🚀 Running Telegram Send File Pipeline...")
    pipeline.run(
        {
            "telegram": {
                "type": "file",
                "chat_id": "YOUR_CHAT_ID",
                "message": file_path,
            }
        }
    )


if __name__ == "__main__":
    main()
