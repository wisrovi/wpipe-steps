from typing import Any, Dict, Optional
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep

@step(
    name="twilio_sms",
    version="v1.0",
    description="Send SMS alerts via Twilio",
    tags=["communication", "twilio", "sms", "sync"]
)
class TwilioSmsStep(BaseStep):
    """
    Step for sending SMS messages using Twilio API.
    """
    
    def __init__(
        self,
        account_sid: str,
        auth_token: str,
        from_number: str,
        to_number: str,
        message: Optional[str] = None,
        message_key: Optional[str] = None,
        response_key: str = "twilio_status",
        name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__(name, version)
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.from_number = from_number
        self.to_number = to_number
        self.message = message
        self.message_key = message_key
        self.response_key = response_key

    @to_obj
    def __call__(self, data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            twilio = self.ensure_dependency("twilio", "twilio-python")
            
            text = self.message or data.get(self.message_key, "wpipe Alert")
            
            client = twilio.rest.Client(self.account_sid, self.auth_token)
            message = client.messages.create(
                body=text,
                from_=self.from_number,
                to=self.to_number
            )
            
            data[self.response_key] = {
                "success": True,
                "message_sid": message.sid,
                "status": message.status,
                "to": self.to_number
            }
            return data
            
        except Exception as e:
            data[self.response_key] = {"success": False, "error": str(e)}
            raise RuntimeError(f"Twilio SMS failed: {str(e)}")
