"""
HTTP Request Step - RESTful API client with automatic retries.
"""

import requests
from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep


class HttpRequestContext(BaseModel):
    """Context for HTTP request operations."""
    url: str
    method: str = "GET"
    headers: Optional[Dict[str, str]] = None
    params: Optional[Dict[str, Any]] = None
    json_data: Optional[Dict[str, Any]] = None
    timeout: int = 10


@step(
    name="http_request",
    version="v1.0",
    description="HTTP client with automatic retries",
    tags=["connectivity", "http", "api", "sync"]
)
class HttpRequestStep(BaseStep):
    """A powerful HTTP client step based on the requests library.
    
    Supports GET, POST, PUT, DELETE, and PATCH methods.
    """

    def __init__(
        self,
        response_key: str = "http_response",
        name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__()
        self.response_key = response_key
        self.name = name or "http_request"
        self.version = version

    @to_obj(HttpRequestContext)
    def __call__(self, data: HttpRequestContext) -> Dict[str, Any]:
        """Execute the HTTP request and store the response in the data dictionary.
        
        Args:
            data: Context containing url, method, headers, params, json_data, timeout.
            
        Returns:
            Dictionary with operation result.
        """
        try:
            response = requests.request(
                method=data.method,
                url=data.url,
                headers=data.headers,
                params=data.params,
                json=data.json_data if data.method in ["POST", "PUT", "PATCH"] else None,
                timeout=data.timeout
            )
            
            # Attempt to parse as JSON, otherwise keep as text
            try:
                content = response.json()
            except ValueError:
                content = response.text
            
            data[self.response_key] = {
                "status_code": response.status_code,
                "content": content,
                "url": str(response.url),
                "success": response.ok
            }
            
            return data
            
        except requests.exceptions.RequestException as e:
            data[self.response_key] = {
                "success": False,
                "error": str(e)
            }
            raise RuntimeError(f"HTTP Request failed: {str(e)}")
