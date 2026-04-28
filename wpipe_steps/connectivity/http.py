import requests
from typing import Any, Dict, Optional, Union
from wpipe_steps.core.base import BaseStep

class HttpRequestStep(BaseStep):
    """
    A powerful HTTP client step based on the requests library.
    Supports GET, POST, PUT, DELETE, and PATCH methods.
    """
    
    def __init__(
        self, 
        url: str, 
        method: str = "GET", 
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, Any]] = None,
        json_data: Optional[Dict[str, Any]] = None,
        response_key: str = "http_response",
        timeout: int = 10,
        name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__(name, version)
        self.url = url
        self.method = method.upper()
        self.headers = headers or {}
        self.params = params or {}
        self.json_data = json_data or {}
        self.response_key = response_key
        self.timeout = timeout

    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Executes the HTTP request and stores the response in the data dictionary.
        """
        try:
            response = requests.request(
                method=self.method,
                url=self.url,
                headers=self.headers,
                params=self.params,
                json=self.json_data if self.method in ["POST", "PUT", "PATCH"] else None,
                timeout=self.timeout
            )
            
            # Attempt to parse as JSON, otherwise keep as text
            try:
                content = response.json()
            except ValueError:
                content = response.text

            data[self.response_key] = {
                "status_code": response.status_code,
                "content": content,
                "url": response.url,
                "success": response.ok
            }
            
            return data
            
        except requests.exceptions.RequestException as e:
            data[self.response_key] = {
                "success": False,
                "error": str(e)
            }
            raise RuntimeError(f"HTTP Request failed: {str(e)}")
