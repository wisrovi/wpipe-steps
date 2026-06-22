from typing import Any, Dict, Optional
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep

@step(
    name="slack_alert",
    version="v1.0",
    description="Send notifications to Slack channels",
    tags=["communication", "slack", "sync"]
)
class SlackAlertStep(BaseStep):
    """
    Step for sending messages to Slack channels using webhooks.
    """
    
    def __init__(
        self,
        webhook_url: str,
        message: Optional[str] = None,
        message_key: Optional[str] = None,
        channel: Optional[str] = None,
        response_key: str = "slack_status",
        name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__(name, version)
        self.webhook_url = webhook_url
        self.message = message
        self.message_key = message_key
        self.channel = channel
        self.response_key = response_key

    @to_obj
    def __call__(self, data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            import requests
            
            text = self.message or data.get(self.message_key, "wpipe Notification")
            
            payload = {"text": text}
            if self.channel:
                payload["channel"] = self.channel
            
            response = requests.post(self.webhook_url, json=payload, timeout=10)
            
            data[self.response_key] = {
                "success": response.status_code == 200,
                "status_code": response.status_code,
                "message": text
            }
            return data
            
        except Exception as e:
            data[self.response_key] = {"success": False, "error": str(e)}
            raise RuntimeError(f"Slack Alert failed: {str(e)}")
