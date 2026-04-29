from typing import Any, Dict, Optional
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep

@step(
    name="twitter_post",
    version="v1.0",
    description="Automated post updates to Twitter",
    tags=["communication", "twitter", "social", "sync"]
)
class TwitterPostStep(BaseStep):
    """
    Step for posting tweets to Twitter using API v2.
    """
    
    def __init__(
        self,
        bearer_token: str,
        message: Optional[str] = None,
        message_key: Optional[str] = None,
        response_key: str = "twitter_status",
        name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__(name, version)
        self.bearer_token = bearer_token
        self.message = message
        self.message_key = message_key
        self.response_key = response_key

    @to_obj
    def __call__(self, data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            import requests
            
            text = self.message or data.get(self.message_key, "")
            
            if len(text) > 280:
                text = text[:277] + "..."
            
            headers = {
                "Authorization": f"Bearer {self.bearer_token}",
                "Content-Type": "application/json"
            }
            
            payload = {"text": text}
            
            response = requests.post(
                "https://api.twitter.com/2/tweets",
                headers=headers,
                json=payload,
                timeout=10
            )
            
            data[self.response_key] = {
                "success": response.status_code == 200,
                "status_code": response.status_code,
                "message": text
            }
            return data
            
        except Exception as e:
            data[self.response_key] = {"success": False, "error": str(e)}
            raise RuntimeError(f"Twitter Post failed: {str(e)}")
