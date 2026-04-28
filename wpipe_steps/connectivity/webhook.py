"""
Webhook Trigger Step - Send data to external services.
"""

import requests
from typing import Any, Dict, Optional
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep


class WebhookContext(BaseModel):
    """Context for webhook operations."""
    webhook_url: str
    payload_key: Optional[str] = None
    custom_payload: Optional[Dict[str, Any]] = None
    headers: Optional[Dict[str, str]] = None


@step(
    name="webhook_trigger",
    version="v1.0",
    description="Webhook notifier",
    tags=["connectivity", "webhook", "notification", "sync"]
)
class WebhookTriggerStep(BaseStep):
    """Step for triggering external webhooks.
    
    Optimized for simple "fire and forget" or basic confirmation notifications.
    """

    def __init__(
        self,
        response_key: str = "webhook_status",
        name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__()
        self.response_key = response_key
        self.name = name or "webhook_trigger"
        self.version = version

    @to_obj(WebhookContext)
    def __call__(self, data: WebhookContext) -> Dict[str, Any]:
        """Trigger the webhook with payload.
        
        Args:
            data: Context containing webhook_url, payload_key, custom_payload, headers.
            
        Returns:
            Dictionary with operation result.
        """
        # Determine payload: specific key from data, custom payload, or entire data
        if data.payload_key:
            payload = data.get(data.payload_key, {})
        elif data.custom_payload:
            payload = data.custom_payload
        else:
            # Avoid circular references or massive objects if sending entire data
            payload = {k: v for k, v in data.items() if isinstance(v, (str, int, float, bool, dict, list))}
        
        try:
            response = requests.post(
                data.webhook_url,
                json=payload,
                headers=data.headers or {"Content-Type": "application/json"},
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
