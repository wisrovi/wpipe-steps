import requests
from typing import Any, Dict, Optional
from wpipe_steps.core.base import BaseStep

class GraphQLQueryStep(BaseStep):
    """
    Step for executing GraphQL queries and mutations.
    """
    
    def __init__(
        self, 
        url: str, 
        query: str, 
        variables: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        response_key: str = "graphql_response",
        timeout: int = 15,
        name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__(name, version)
        self.url = url
        self.query = query
        self.variables = variables or {}
        self.headers = headers or {}
        self.response_key = response_key
        self.timeout = timeout

    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        payload = {
            "query": self.query,
            "variables": self.variables
        }
        
        try:
            response = requests.post(
                self.url,
                json=payload,
                headers=self.headers,
                timeout=self.timeout
            )
            
            result = response.json()
            
            data[self.response_key] = {
                "status_code": response.status_code,
                "data": result.get("data"),
                "errors": result.get("errors"),
                "success": response.ok and "errors" not in result
            }
            
            return data
            
        except Exception as e:
            data[self.response_key] = {
                "success": False,
                "error": str(e)
            }
            raise RuntimeError(f"GraphQL Query failed: {str(e)}")
