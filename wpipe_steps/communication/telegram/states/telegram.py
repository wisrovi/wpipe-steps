from typing import Any, Dict, Optional
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wconnect import Wtelegram
from wauth import WAuth


class BaseTelegramStep(BaseStep):
    """
    Base class for Telegram steps handling client initialization and authentication.
    """

    def __init__(
        self,
        bot_token: Optional[str] = None,
        chat_id: Optional[str] = None,
        auth_instance: Optional[Any] = None,
        db_path: str = "wauth_telegram.db",
        chat_id_key: Optional[str] = None,
        response_key: str = "telegram_status",
        name: Optional[str] = None,
        version: str = "v1.0",
    ):
        super().__init__(name, version)
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.db_path = db_path
        self.auth_instance = auth_instance
        self.chat_id_key = chat_id_key
        self.response_key = response_key

    def _get_val(self, obj: Any, key: str, default: Any = None) -> Any:
        """Helper to safely extract a key/attribute from a dict or object."""
        if obj is None or not key:
            return default
        if isinstance(obj, dict):
            return obj.get(key, default)
        return getattr(obj, key, default)

    def _extract_from_data(self, data: Any, key: Optional[str]) -> Any:
        """Helper to extract a value from data, supporting dot notation for nested dicts/objects."""
        if not key or data is None:
            return None
        parts = key.split(".")
        curr = data
        for part in parts:
            if curr is None:
                return None
            curr = self._get_val(curr, part)
        return curr

    def _get_chat_id(self, data: Any) -> Optional[str]:
        extracted = (
            self._extract_from_data(data, self.chat_id_key)
            if self.chat_id_key
            else None
        )
        telegram_data = self._get_val(data, "telegram")
        if not extracted and telegram_data:
            extracted = self._get_val(telegram_data, "chat_id")
        return self.chat_id or extracted or self._get_val(data, "chat_id")

    def _set_response(self, data: Any, val: Dict[str, Any]) -> Any:
        """Helper to set response_key in dict or object."""
        if isinstance(data, dict):
            data[self.response_key] = val
        else:
            setattr(data, self.response_key, val)
        return data

    def _get_client(self, chat_id: Optional[str] = None) -> Wtelegram:
        auth = self.auth_instance
        if auth is None and not self.bot_token:
            auth = WAuth(db_path=self.db_path)

        return Wtelegram(token=self.bot_token, auth_instance=auth)


@step(
    name="telegram_send_text",
    version="v1.0",
    description="Send text messages via Telegram using Wtelegram",
    tags=["communication", "telegram", "text", "sync"],
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
        db_path: str = "wauth_telegram.db",
        message: Optional[str] = None,
        message_key: Optional[str] = None,
        chat_id_key: Optional[str] = None,
        response_key: str = "telegram_status",
        name: Optional[str] = None,
        version: str = "v1.0",
    ):
        super().__init__(
            bot_token=bot_token,
            chat_id=chat_id,
            auth_instance=auth_instance,
            db_path=db_path,
            chat_id_key=chat_id_key,
            response_key=response_key,
            name=name,
            version=version,
        )
        self.message = message
        self.message_key = message_key

    @to_obj
    def __call__(self, data: Any) -> Any:
        try:
            target_chat_id = self._get_chat_id(data)
            extracted_msg = (
                self._extract_from_data(data, self.message_key)
                if self.message_key
                else None
            )
            telegram_data = self._get_val(data, "telegram")
            if not extracted_msg and telegram_data:
                extracted_msg = self._get_val(telegram_data, "message")

            text = (
                self.message
                or extracted_msg
                or self._get_val(data, "message")
                or "WPipe Notification"
            )

            with self._get_client(target_chat_id) as sender:
                response = sender.send(to=target_chat_id, message=text)

            return self._set_response(
                data,
                {
                    "success": bool(response),
                    "message_sent": text,
                    "response": str(response),
                },
            )

        except Exception as e:
            self._set_response(data, {"success": False, "error": str(e)})
            raise RuntimeError(f"Telegram Text Notification failed: {str(e)}")


@step(
    name="telegram_send_image",
    version="v1.0",
    description="Send image/photo via Telegram using Wtelegram",
    tags=["communication", "telegram", "image", "sync"],
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
        db_path: str = "wauth_telegram.db",
        image_path: Optional[str] = None,
        image_path_key: Optional[str] = None,
        caption: Optional[str] = None,
        caption_key: Optional[str] = None,
        chat_id_key: Optional[str] = None,
        response_key: str = "telegram_status",
        name: Optional[str] = None,
        version: str = "v1.0",
    ):
        super().__init__(
            bot_token=bot_token,
            chat_id=chat_id,
            auth_instance=auth_instance,
            db_path=db_path,
            chat_id_key=chat_id_key,
            response_key=response_key,
            name=name,
            version=version,
        )
        self.image_path = image_path
        self.image_path_key = image_path_key
        self.caption = caption
        self.caption_key = caption_key

    @to_obj
    def __call__(self, data: Any) -> Any:
        try:
            target_chat_id = self._get_chat_id(data)
            extracted_path = (
                self._extract_from_data(data, self.image_path_key)
                if self.image_path_key
                else None
            )
            telegram_data = self._get_val(data, "telegram")
            if not extracted_path and telegram_data:
                extracted_path = (
                    self._get_val(telegram_data, "message")
                    or self._get_val(telegram_data, "path")
                    or self._get_val(telegram_data, "image_path")
                )

            path = (
                self.image_path or extracted_path or self._get_val(data, "image_path")
            )
            if not path:
                raise ValueError(
                    "Image path is required either via image_path parameter or data dict"
                )

            extracted_caption = (
                self._extract_from_data(data, self.caption_key)
                if self.caption_key
                else None
            )
            if not extracted_caption and telegram_data:
                extracted_caption = self._get_val(telegram_data, "caption")

            text = self.caption or extracted_caption

            with self._get_client(target_chat_id) as sender:
                response = sender.send_photo(
                    to=target_chat_id, photo=path, caption=text
                )

            return self._set_response(
                data,
                {
                    "success": bool(response),
                    "image_sent": path,
                    "caption": text,
                    "response": str(response),
                },
            )

        except Exception as e:
            self._set_response(data, {"success": False, "error": str(e)})
            raise RuntimeError(f"Telegram Image Notification failed: {str(e)}")


@step(
    name="telegram_send_file",
    version="v1.0",
    description="Send generic documents/files via Telegram using Wtelegram",
    tags=["communication", "telegram", "file", "sync"],
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
        db_path: str = "wauth_telegram.db",
        file_path: Optional[str] = None,
        file_path_key: Optional[str] = None,
        caption: Optional[str] = None,
        caption_key: Optional[str] = None,
        chat_id_key: Optional[str] = None,
        response_key: str = "telegram_status",
        name: Optional[str] = None,
        version: str = "v1.0",
    ):
        super().__init__(
            bot_token=bot_token,
            chat_id=chat_id,
            auth_instance=auth_instance,
            db_path=db_path,
            chat_id_key=chat_id_key,
            response_key=response_key,
            name=name,
            version=version,
        )
        self.file_path = file_path
        self.file_path_key = file_path_key
        self.caption = caption
        self.caption_key = caption_key

    @to_obj
    def __call__(self, data: Any) -> Any:
        try:
            target_chat_id = self._get_chat_id(data)
            extracted_path = (
                self._extract_from_data(data, self.file_path_key)
                if self.file_path_key
                else None
            )
            telegram_data = self._get_val(data, "telegram")
            if not extracted_path and telegram_data:
                extracted_path = (
                    self._get_val(telegram_data, "message")
                    or self._get_val(telegram_data, "path")
                    or self._get_val(telegram_data, "file_path")
                )

            path = self.file_path or extracted_path or self._get_val(data, "file_path")
            if not path:
                raise ValueError(
                    "File path is required either via file_path parameter or data dict"
                )

            extracted_caption = (
                self._extract_from_data(data, self.caption_key)
                if self.caption_key
                else None
            )
            if not extracted_caption and telegram_data:
                extracted_caption = self._get_val(telegram_data, "caption")

            text = self.caption or extracted_caption

            with self._get_client(target_chat_id) as sender:
                response = sender.send_document(
                    to=target_chat_id, path=path, caption=text
                )

            return self._set_response(
                data,
                {
                    "success": bool(response),
                    "file_sent": path,
                    "caption": text,
                    "response": str(response),
                },
            )

        except Exception as e:
            self._set_response(data, {"success": False, "error": str(e)})
            raise RuntimeError(f"Telegram File Notification failed: {str(e)}")


@step(
    name="telegram_notify",
    version="v1.0",
    description="Send messages, images, or files via Telegram dynamically using Wtelegram",
    tags=["communication", "telegram", "dispatcher", "sync"],
)
class TelegramNotifyStep(BaseTelegramStep):
    """
    Unified step for sending text, images, or files via Telegram dynamically using Wtelegram.
    Reads `data['telegram']['type']` ('text', 'image', 'file') to dispatch appropriately.
    """

    def __init__(
        self,
        bot_token: Optional[str] = None,
        chat_id: Optional[str] = None,
        auth_instance: Optional[Any] = None,
        db_path: str = "wauth_telegram.db",
        message: Optional[str] = None,
        message_key: Optional[str] = None,
        chat_id_key: Optional[str] = None,
        response_key: str = "telegram_status",
        name: Optional[str] = None,
        version: str = "v1.0",
    ):
        super().__init__(
            bot_token=bot_token,
            chat_id=chat_id,
            auth_instance=auth_instance,
            db_path=db_path,
            chat_id_key=chat_id_key,
            response_key=response_key,
            name=name,
            version=version,
        )
        self.message = message
        self.message_key = message_key

    @to_obj
    def __call__(self, data: Any) -> Any:
        telegram_data = self._get_val(data, "telegram")
        msg_type = (self._get_val(telegram_data, "type", "text") or "text").lower()

        if msg_type in ("image", "photo"):
            step = TelegramSendImageStep(
                bot_token=self.bot_token,
                chat_id=self.chat_id,
                auth_instance=self.auth_instance,
                db_path=self.db_path,
                chat_id_key=self.chat_id_key,
                response_key=self.response_key,
            )
            return step(data)

        elif msg_type in ("file", "document"):
            step = TelegramSendFileStep(
                bot_token=self.bot_token,
                chat_id=self.chat_id,
                auth_instance=self.auth_instance,
                db_path=self.db_path,
                chat_id_key=self.chat_id_key,
                response_key=self.response_key,
            )
            return step(data)

        else:
            step = TelegramSendTextStep(
                bot_token=self.bot_token,
                chat_id=self.chat_id,
                auth_instance=self.auth_instance,
                db_path=self.db_path,
                message=self.message,
                message_key=self.message_key,
                chat_id_key=self.chat_id_key,
                response_key=self.response_key,
            )
            return step(data)
