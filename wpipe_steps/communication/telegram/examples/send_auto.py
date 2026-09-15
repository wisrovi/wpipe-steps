import os
from wpipe import Pipeline
from wpipe_steps.communication import TelegramNotifyStep


def print_result(data):
    """Step to print Telegram dispatcher result."""
    status = data.get("telegram_status", {})
    if status.get("success"):
        print(f"✅ Telegram Action Succeeded: {status}")
    else:
        print(f"❌ Telegram Action Failed: {status.get('error')}")
    return data


def main():
    media_dir = os.path.dirname(os.path.abspath(__file__))
    image_file = os.path.join(media_dir, "media", "demo.png")
    csv_file = os.path.join(media_dir, "media", "demo.csv")

    pipeline_text = Pipeline(pipeline_name="Telegram_Text_Auto_Demo", verbose=True)
    pipeline_image = Pipeline(pipeline_name="Telegram_Image_Auto_Demo", verbose=True)
    pipeline_file = Pipeline(pipeline_name="Telegram_File_Auto_Demo", verbose=True)

    # All pipelines use the single dynamic dispatcher step TelegramNotifyStep
    pipeline_text.set_steps(
        [
            TelegramNotifyStep(
                name="Send_Telegram_Dynamic",
                bot_token="YOUR_BOT_TOKEN",
            ),
            print_result,
        ]
    )

    pipeline_image.set_steps(
        [
            TelegramNotifyStep(
                name="Send_Telegram_Dynamic",
                bot_token="YOUR_BOT_TOKEN",
            ),
            print_result,
        ]
    )

    pipeline_file.set_steps(
        [
            TelegramNotifyStep(
                name="Send_Telegram_Dynamic",
                bot_token="YOUR_BOT_TOKEN",
            ),
            print_result,
        ]
    )

    print("🚀 Running Telegram Dynamic Dispatcher Examples...")

    # 1. Dispatcher automatically handles text
    pipeline_text.run(
        {
            "telegram": {
                "type": "text",
                "message": "Hello from the dynamic Telegram dispatcher example!",
                "chat_id": "YOUR_CHAT_ID",
            }
        }
    )

    # 2. Dispatcher automatically handles image
    pipeline_image.run(
        {
            "telegram": {
                "type": "image",
                "chat_id": "YOUR_CHAT_ID",
                "caption": "Test image dispatched dynamically.",
                "message": image_file,
            }
        }
    )

    # 3. Dispatcher automatically handles file
    pipeline_file.run(
        {
            "telegram": {
                "type": "file",
                "chat_id": "YOUR_CHAT_ID",
                "message": csv_file,
            }
        }
    )


if __name__ == "__main__":
    main()
