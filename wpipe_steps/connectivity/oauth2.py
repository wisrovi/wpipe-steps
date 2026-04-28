import requests
import time
from typing import Any, Dict, Optional
from wpipe_steps.core.base import BaseStep

class OAuth2AuthStep(BaseStep):
    """
    Step for handling OAuth2 Client Credentials flow.
    Retrieves and manages access tokens for API authentication.
    """
    
    def __init__(
        self, 
        token_url: str, 
        client_id: str, 
        client_secret: str,
        scope: Optional[str] = None,
        response_key: str = "oauth_token",
        name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__(name, version)
        self.token_url = token_url
        self.client_id = client_id
        self.client_secret = client_secret
        self.scope = scope
        self.response_key = response_key

    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        payload = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret
        }
        if self.scope:
            payload["scope"] = self.scope

        try:
            response = requests.post(
                self.token_url,
                data=payload,
                timeout=10
            )
            
            result = response.json()
            
            if not response.ok:
                raise RuntimeError(f"OAuth2 failed: {result.get('error_description', result.get('error', 'Unknown error'))}")

            # Store token and metadata
            data[self.response_key] = {
                "access_token": result.get("access_token"),
                "token_type": result.get("token_type", "Bearer"),
                "expires_in": result.get("expires_in"),
                "retrieved_at": time.time(),
                "success": True
            }
            
            # Helper for subsequent steps: add directly to common auth headers
            if "auth_headers" not in data:
                data["auth_headers"] = {}
            
            data["auth_headers"]["Authorization"] = f"{result.get('token_type', 'Bearer')} {result.get('access_token')}"
            
            return data
            
        except Exception as e:
            data[self.response_key] = {
                "success": False,
                "error": str(e)
            }
            raise RuntimeError(f"OAuth2 Authentication failed: {str(e)}")
