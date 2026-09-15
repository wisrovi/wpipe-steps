import os
from wpipe import Pipeline
from wpipe_steps.communication import TelegramSendImageStep


def print_result(data):
    """Step to print Telegram image result."""
    status = data.get("telegram_status", {})
    if status.get("success"):
        print(f"✅ Telegram Image Sent: {status.get('image_sent')}")
    else:
        print(f"❌ Telegram Image Failed: {status.get('error')}")
    return data


def main():
    pipeline = Pipeline(pipeline_name="Telegram_Send_Image_Demo", verbose=True)

    media_dir = os.path.dirname(os.path.abspath(__file__))
    image_file = os.path.join(media_dir, "media", "demo.png")

    pipeline.set_steps(
        [
            TelegramSendImageStep(
                name="Send_Telegram_Image",
                bot_token="YOUR_BOT_TOKEN",
            ),
            print_result,
        ]
    )

    print("🚀 Running Telegram Send Image Pipeline...")
    pipeline.run(
        {
            "telegram": {
                "type": "image",
                "chat_id": "YOUR_CHAT_ID",
                "caption": "This is a test image sent from the Telegram pipeline example.",
                "message": image_file,
            }
        }
    )


if __name__ == "__main__":
    main()
