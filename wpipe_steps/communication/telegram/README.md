# 🧱 Telegram Steps (WPipe)

Send text messages, images, and files via Telegram using `wconnect.wmessenger.Wtelegram`.

## 🛠️ Key Technologies & Dependencies

- **Python 3.10+**
- **[wconnect / wmessenger](https://pypi.org/project/wconnect/)**: Unified messaging engine (`Wtelegram`) for Telegram integration.
- **WPipe Framework**: Base step class (`BaseStep`) and `@step` decorators.

## 📂 Structure

This step follows the WPipe professional package structure:
- `config/`: Configuration constants.
- `examples/`: Code examples for text, image, and file steps.
- `exceptions/`: Custom step exceptions.
- `schemas/`: Pydantic input/output schemas.
- `states/`: Actual step execution logic (`TelegramSendTextStep`, `TelegramSendImageStep`, `TelegramSendFileStep`).
- `utils/`: Internal helper utilities.
- `wrappers/`: Third-party library wrappers.

## ⚙️ Configuration

Namespace: `wpipe_steps.communication.telegram`

## 🚀 Available Steps

### 1. `TelegramSendTextStep` (Alias: `TelegramNotifyStep`)
Sends text messages via Telegram.

```python
from wpipe_steps.communication.telegram import TelegramSendTextStep

step = TelegramSendTextStep.as_step(
    name="Send_Text",
    bot_token="YOUR_BOT_TOKEN",
    chat_id="YOUR_CHAT_ID",
    message="Hello from WPipe!",
)
```

### 2. `TelegramSendImageStep`
Sends photos/images via Telegram.

```python
from wpipe_steps.communication.telegram import TelegramSendImageStep

step = TelegramSendImageStep.as_step(
    name="Send_Image",
    bot_token="YOUR_BOT_TOKEN",
    chat_id="YOUR_CHAT_ID",
    image_path="/path/to/image.png",
    caption="Here is the chart result",
)
```

### 3. `TelegramSendFileStep`
Sends documents or general files via Telegram.

```python
from wpipe_steps.communication.telegram import TelegramSendFileStep

step = TelegramSendFileStep.as_step(
    name="Send_File",
    bot_token="YOUR_BOT_TOKEN",
    chat_id="YOUR_CHAT_ID",
    file_path="/path/to/report.pdf",
    caption="Monthly report PDF",
)
```

