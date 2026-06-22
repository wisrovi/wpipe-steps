from typing import Any, Dict, Optional, List
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep

@step(
    name="discord_bot",
    version="v1.0",
    description="Send embeds to Discord servers",
    tags=["communication", "discord", "sync"]
)
class DiscordBotStep(BaseStep):
    """
    Step for sending messages/embeds to Discord channels using webhooks.
    """
    
    def __init__(
        self,
        webhook_url: str,
        message: Optional[str] = None,
        message_key: Optional[str] = None,
        embeds: Optional[List[Dict]] = None,
        response_key: str = "discord_status",
        name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__(name, version)
        self.webhook_url = webhook_url
        self.message = message
        self.message_key = message_key
        self.embeds = embeds
        self.response_key = response_key

    @to_obj
    def __call__(self, data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            import requests
            
            text = self.message or data.get(self.message_key, "wpipe Notification")
            
            payload = {"content": text}
            if self.embeds:
                payload["embeds"] = self.embeds
            
            response = requests.post(self.webhook_url, json=payload, timeout=10)
            
            data[self.response_key] = {
                "success": response.status_code in [200, 204],
                "status_code": response.status_code,
                "message": text
            }
            return data
            
        except Exception as e:
            data[self.response_key] = {"success": False, "error": str(e)}
            raise RuntimeError(f"Discord Bot failed: {str(e)}")
