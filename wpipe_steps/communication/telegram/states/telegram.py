from typing import Any, Dict, Optional
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wconnect import Wtelegram


class BaseTelegramStep(BaseStep):
    """
    Base class for Telegram steps handling client initialization and authentication.
    """

    def __init__(
        self,
        bot_token: Optional[str] = None,
        chat_id: Optional[str] = None,
        auth_instance: Optional[Any] = None,
        chat_id_key: Optional[str] = None,
        response_key: str = "telegram_status",
        name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__(name, version)
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.auth_instance = auth_instance
        self.chat_id_key = chat_id_key
        self.response_key = response_key

    def _extract_from_data(self, data: Dict[str, Any], key: Optional[str]) -> Any:
        """Helper to extract a value from data, supporting dot notation for nested dicts."""
        if not key or not data:
            return None
        parts = key.split(".")
        curr = data
        for part in parts:
            if isinstance(curr, dict) and part in curr:
                curr = curr[part]
            else:
                return None
        return curr

    def _get_chat_id(self, data: Dict[str, Any]) -> Optional[str]:
        extracted = self._extract_from_data(data, self.chat_id_key) if self.chat_id_key else None
        if not extracted and isinstance(data.get("telegram"), dict):
            extracted = data["telegram"].get("chat_id")
        return self.chat_id or extracted or data.get("chat_id")

    def _get_client(self, chat_id: Optional[str] = None) -> Wtelegram:
        return Wtelegram(
            bot_token=self.bot_token,
            chat_id=chat_id or self.chat_id,
            auth_instance=self.auth_instance
        )


@step(
    name="telegram_send_text",
    version="v1.0",
    description="Send text messages via Telegram using Wtelegram",
    tags=["communication", "telegram", "text", "sync"]
)
class TelegramSendTextStep(BaseTelegramStep):
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
        super().__init__(
            bot_token=bot_token,
            chat_id=chat_id,
            auth_instance=auth_instance,
            chat_id_key=chat_id_key,
            response_key=response_key,
            name=name,
            version=version
        )
        self.message = message
        self.message_key = message_key

    @to_obj
    def __call__(self, data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            target_chat_id = self._get_chat_id(data)
            extracted_msg = self._extract_from_data(data, self.message_key) if self.message_key else None
            if not extracted_msg and isinstance(data.get("telegram"), dict):
                extracted_msg = data["telegram"].get("message")
            
            text = self.message or extracted_msg or data.get("message") or "WPipe Notification"

            with self._get_client(target_chat_id) as sender:
                response = sender.send_text(text=text, chat_id=target_chat_id)

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
class TelegramSendImageStep(BaseTelegramStep):
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
        super().__init__(
            bot_token=bot_token,
            chat_id=chat_id,
            auth_instance=auth_instance,
            chat_id_key=chat_id_key,
            response_key=response_key,
            name=name,
            version=version
        )
        self.image_path = image_path
        self.image_path_key = image_path_key
        self.caption = caption
        self.caption_key = caption_key

    @to_obj
    def __call__(self, data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            target_chat_id = self._get_chat_id(data)
            extracted_path = self._extract_from_data(data, self.image_path_key) if self.image_path_key else None
            if not extracted_path and isinstance(data.get("telegram"), dict):
                extracted_path = data["telegram"].get("message") or data["telegram"].get("path") or data["telegram"].get("image_path")

            path = self.image_path or extracted_path or data.get("image_path")
            if not path:
                raise ValueError("Image path is required either via image_path parameter or data dict")

            extracted_caption = self._extract_from_data(data, self.caption_key) if self.caption_key else None
            if not extracted_caption and isinstance(data.get("telegram"), dict):
                extracted_caption = data["telegram"].get("caption")

            text = self.caption or extracted_caption

            with self._get_client(target_chat_id) as sender:
                response = sender.send_photo(photo_path=path, caption=text, chat_id=target_chat_id)

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
class TelegramSendFileStep(BaseTelegramStep):
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
        super().__init__(
            bot_token=bot_token,
            chat_id=chat_id,
            auth_instance=auth_instance,
            chat_id_key=chat_id_key,
            response_key=response_key,
            name=name,
            version=version
        )
        self.file_path = file_path
        self.file_path_key = file_path_key
        self.caption = caption
        self.caption_key = caption_key

    @to_obj
    def __call__(self, data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            target_chat_id = self._get_chat_id(data)
            extracted_path = self._extract_from_data(data, self.file_path_key) if self.file_path_key else None
            if not extracted_path and isinstance(data.get("telegram"), dict):
                extracted_path = data["telegram"].get("message") or data["telegram"].get("path") or data["telegram"].get("file_path")

            path = self.file_path or extracted_path or data.get("file_path")
            if not path:
                raise ValueError("File path is required either via file_path parameter or data dict")

            extracted_caption = self._extract_from_data(data, self.caption_key) if self.caption_key else None
            if not extracted_caption and isinstance(data.get("telegram"), dict):
                extracted_caption = data["telegram"].get("caption")

            text = self.caption or extracted_caption

            with self._get_client(target_chat_id) as sender:
                response = sender.send_document(document_path=path, caption=text, chat_id=target_chat_id)

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




