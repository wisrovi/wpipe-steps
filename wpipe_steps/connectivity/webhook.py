import requests
from typing import Any, Dict, Optional
from wpipe_steps.core.base import BaseStep

class WebhookTriggerStep(BaseStep):
    """
    Step for triggering external webhooks.
    Optimized for simple "fire and forget" or basic confirmation notifications.
    """
    
    def __init__(
        self, 
        webhook_url: str, 
        payload_key: Optional[str] = None,
        custom_payload: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        response_key: str = "webhook_status",
        name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__(name, version)
        self.webhook_url = webhook_url
        self.payload_key = payload_key
        self.custom_payload = custom_payload
        self.headers = headers or {"Content-Type": "application/json"}
        self.response_key = response_key

    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        # Determine payload: specific key from data, custom payload, or entire data
        if self.payload_key:
            payload = data.get(self.payload_key, {})
        elif self.custom_payload:
            payload = self.custom_payload
        else:
            # Avoid circular references or massive objects if sending entire data
            payload = {k: v for k, v in data.items() if isinstance(v, (str, int, float, bool, dict, list))}

        try:
            response = requests.post(
                self.webhook_url,
                json=payload,
                headers=self.headers,
                timeout=10
            )
            
            data[self.response_key] = {
                "sent": True,
                "status_code": response.status_code,
                "success": response.ok
            }
            
            return data
            
        except Exception as e:
            data[self.response_key] = {
                "sent": False,
                "error": str(e)
            }
            raise RuntimeError(f"Webhook Trigger failed: {str(e)}")
