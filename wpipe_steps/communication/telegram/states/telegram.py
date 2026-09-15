from typing import Any, Dict, Optional
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wconnect import Wtelegram



@step(
    name="telegram_send_text",
    version="v1.0",
    description="Send text messages via Telegram using Wtelegram",
    tags=["communication", "telegram", "text", "sync"]
)
class TelegramSendTextStep(BaseStep):
    """
    Step for sending text messages via Telegram using Wtelegram.
    """

    def __init__(
        self,
        bot_token: Optional[str] = None,
        chat_id: Optional[str] = None,
        auth_instance: Optional[Any] = None,
        message: Optional[str] = None,
        message_key: Optional[str] = None,
        chat_id_key: Optional[str] = None,
        response_key: str = "telegram_status",
        name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__(name, version)
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.auth_instance = auth_instance
        self.message = message
        self.message_key = message_key
        self.chat_id_key = chat_id_key
        self.response_key = response_key

    @to_obj
    def __call__(self, data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            chat_id = self.chat_id or data.get(self.chat_id_key) if self.chat_id_key else self.chat_id
            text = self.message or (data.get(self.message_key) if self.message_key else None) or "WPipe Notification"

            with Wtelegram(bot_token=self.bot_token, chat_id=chat_id, auth_instance=self.auth_instance) as sender:
                response = sender.send_text(text=text, chat_id=chat_id)

            data[self.response_key] = {
                "success": True,
                "message_sent": text,
                "response": str(response)
            }
            return data

        except Exception as e:
            data[self.response_key] = {"success": False, "error": str(e)}
            raise RuntimeError(f"Telegram Text Notification failed: {str(e)}")


@step(
    name="telegram_send_image",
    version="v1.0",
    description="Send image/photo via Telegram using Wtelegram",
    tags=["communication", "telegram", "image", "sync"]
)
class TelegramSendImageStep(BaseStep):
    """
    Step for sending photos via Telegram using Wtelegram.
    """

    def __init__(
        self,
        bot_token: Optional[str] = None,
        chat_id: Optional[str] = None,
        auth_instance: Optional[Any] = None,
        image_path: Optional[str] = None,
        image_path_key: Optional[str] = None,
        caption: Optional[str] = None,
        caption_key: Optional[str] = None,
        chat_id_key: Optional[str] = None,
        response_key: str = "telegram_status",
        name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__(name, version)
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.auth_instance = auth_instance
        self.image_path = image_path
        self.image_path_key = image_path_key
        self.caption = caption
        self.caption_key = caption_key
        self.chat_id_key = chat_id_key
        self.response_key = response_key

    @to_obj
    def __call__(self, data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            chat_id = self.chat_id or data.get(self.chat_id_key) if self.chat_id_key else self.chat_id
            path = self.image_path or (data.get(self.image_path_key) if self.image_path_key else None)
            if not path:
                raise ValueError("Image path is required either via image_path or data[image_path_key]")

            text = self.caption or (data.get(self.caption_key) if self.caption_key else None)

            with Wtelegram(bot_token=self.bot_token, chat_id=chat_id, auth_instance=self.auth_instance) as sender:
                response = sender.send_photo(photo_path=path, caption=text, chat_id=chat_id)

            data[self.response_key] = {
                "success": True,
                "image_sent": path,
                "caption": text,
                "response": str(response)
            }
            return data

        except Exception as e:
            data[self.response_key] = {"success": False, "error": str(e)}
            raise RuntimeError(f"Telegram Image Notification failed: {str(e)}")


@step(
    name="telegram_send_file",
    version="v1.0",
    description="Send generic documents/files via Telegram using Wtelegram",
    tags=["communication", "telegram", "file", "sync"]
)
class TelegramSendFileStep(BaseStep):
    """
    Step for sending generic files/documents via Telegram using Wtelegram.
    """

    def __init__(
        self,
        bot_token: Optional[str] = None,
        chat_id: Optional[str] = None,
        auth_instance: Optional[Any] = None,
        file_path: Optional[str] = None,
        file_path_key: Optional[str] = None,
        caption: Optional[str] = None,
        caption_key: Optional[str] = None,
        chat_id_key: Optional[str] = None,
        response_key: str = "telegram_status",
        name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__(name, version)
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.auth_instance = auth_instance
        self.file_path = file_path
        self.file_path_key = file_path_key
        self.caption = caption
        self.caption_key = caption_key
        self.chat_id_key = chat_id_key
        self.response_key = response_key

    @to_obj
    def __call__(self, data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            chat_id = self.chat_id or data.get(self.chat_id_key) if self.chat_id_key else self.chat_id
            path = self.file_path or (data.get(self.file_path_key) if self.file_path_key else None)
            if not path:
                raise ValueError("File path is required either via file_path or data[file_path_key]")

            text = self.caption or (data.get(self.caption_key) if self.caption_key else None)

            with Wtelegram(bot_token=self.bot_token, chat_id=chat_id, auth_instance=self.auth_instance) as sender:
                response = sender.send_document(document_path=path, caption=text, chat_id=chat_id)

            data[self.response_key] = {
                "success": True,
                "file_sent": path,
                "caption": text,
                "response": str(response)
            }
            return data

        except Exception as e:
            data[self.response_key] = {"success": False, "error": str(e)}
            raise RuntimeError(f"Telegram File Notification failed: {str(e)}")


# Alias for backward compatibility
TelegramNotifyStep = TelegramSendTextStep

