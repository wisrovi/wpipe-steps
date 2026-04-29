from typing import Any, Dict, Optional
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep

@step(
    name="telegram_notify",
    version="v1.0",
    description="Send messages/alerts via Telegram",
    tags=["communication", "telegram", "sync"]
)
class TelegramNotifyStep(BaseStep):
    """
    Step for sending notifications via Telegram using wconnect or direct API.
    """
    
    def __init__(
        self, 
        bot_token: str,
        chat_id: str,
        message: Optional[str] = None,
        message_key: Optional[str] = None,
        response_key: str = "telegram_status",
        name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__(name, version)
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.message = message
        self.message_key = message_key
        self.response_key = response_key

    @to_obj
    def __call__(self, data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            import requests
            
            text = self.message or data.get(self.message_key, "WPipe Notification")
            
            url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
            payload = {
                "chat_id": self.chat_id,
                "text": text,
                "parse_mode": "HTML"
            }
            
            response = requests.post(url, json=payload, timeout=10)
            result = response.json()
            
            data[self.response_key] = {
                "success": result.get("ok", False),
                "status_code": response.status_code,
                "message_sent": text
            }
            return data
            
        except Exception as e:
            data[self.response_key] = {"success": False, "error": str(e)}
            raise RuntimeError(f"Telegram Notification failed: {str(e)}")
