from wpipe import Pipeline
from wpipe_steps.communication import (
    TelegramSendTextStep,
    TelegramSendImageStep,
    TelegramSendFileStep,
)


def print_result(data):
    """Step to print Telegram result."""
    status = data.get("telegram_status", {})
    if status.get("success"):
        print(f"✅ Telegram Action Succeeded: {status}")
    else:
        print(f"❌ Telegram Action Failed: {status.get('error')}")
    return data


def main():
    pipeline = Pipeline(pipeline_name="Telegram_Demo", verbose=True)

    # Example 1: Text step
    send_text = TelegramSendTextStep.as_step(
        name="Send_Telegram_Text",
        bot_token="YOUR_BOT_TOKEN",
        chat_id="YOUR_CHAT_ID",
        message="🚀 Pipeline completed successfully!",
    )

    # Example 2: Image step
    send_image = TelegramSendImageStep.as_step(
        name="Send_Telegram_Image",
        bot_token="YOUR_BOT_TOKEN",
        chat_id="YOUR_CHAT_ID",
        image_path="/path/to/image.png",
        caption="Pipeline chart result",
    )

    # Example 3: File step
    send_file = TelegramSendFileStep.as_step(
        name="Send_Telegram_File",
        bot_token="YOUR_BOT_TOKEN",
        chat_id="YOUR_CHAT_ID",
        file_path="/path/to/document.pdf",
        caption="Pipeline execution report",
    )

    pipeline.set_steps([send_text, print_result])

    print("🚀 Starting Telegram Demo Pipeline...")
    pipeline.run({})


if __name__ == "__main__":
    main()

