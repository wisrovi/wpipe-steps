from typing import Any, Dict, Optional
from wpipe_steps.core.base import BaseStep

class TelegramNotifyStep(BaseStep):
    """
    Step for sending notifications via Telegram using wconnect.
    """
    
    def __init__(
        self, 
        bot_token: str,
        chat_id: str,
        message: Optional[str] = None,
        message_key: Optional[str] = None, # Key in 'data' containing the msg
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

    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        wconnect = self.ensure_dependency("wconnect")
        
        # Determine message
        text = self.message or data.get(self.message_key, "WPipe Notification")
        
        try:
            # Assuming wconnect has a Telegram class or sender
            # Using basic requests implementation as fallback if wconnect is not generic
            import requests
            url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
            payload = {
                "chat_id": self.chat_id,
                "text": text,
                "parse_mode": "HTML"
            }
            response = requests.post(url, json=payload, timeout=10)
            
            data[self.response_key] = {
                "success": response.ok,
                "status_code": response.status_code,
                "message_sent": text
            }
            return data
            
        except Exception as e:
            data[self.response_key] = {"success": False, "error": str(e)}
            raise RuntimeError(f"Telegram Notification failed: {str(e)}")
