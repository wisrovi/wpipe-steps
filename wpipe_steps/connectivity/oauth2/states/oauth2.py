"""
OAuth2 Auth Step - Handle OAuth2 client credentials flow.
"""

import requests
import time
from typing import Any, Dict, Optional
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep


class OAuth2Context(BaseModel):
    """Context for OAuth2 operations."""
    token_url: str
    client_id: str
    client_secret: str
    scope: Optional[str] = None


@step(
    name="oauth2_auth",
    version="v1.0",
    description="OAuth2 token manager",
    tags=["connectivity", "oauth2", "auth", "sync"]
)
class OAuth2AuthStep(BaseStep):
    """Step for handling OAuth2 Client Credentials flow.
    
    Retrieves and manages access tokens for API authentication.
    """

    def __init__(
        self,
        response_key: str = "oauth_token",
        name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__()
        self.response_key = response_key
        self.name = name or "oauth2_auth"
        self.version = version

    @to_obj(OAuth2Context)
    def __call__(self, data: OAuth2Context) -> Dict[str, Any]:
        """Retrieve OAuth2 token.
        
        Args:
            data: Context containing token_url, client_id, client_secret, scope.
            
        Returns:
            Dictionary with operation result.
        """
        payload = {
            "grant_type": "client_credentials",
            "client_id": data.client_id,
            "client_secret": data.client_secret
        }
        if data.scope:
            payload["scope"] = data.scope
        
        try:
            response = requests.post(
                data.token_url,
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
