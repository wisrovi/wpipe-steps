"""
GraphQL Query Step - Execute GraphQL queries and mutations.
"""

import requests
from typing import Any, Dict, Optional
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep


class GraphQLContext(BaseModel):
    """Context for GraphQL operations."""
    url: str
    query: str
    variables: Optional[Dict[str, Any]] = None
    headers: Optional[Dict[str, str]] = None
    timeout: int = 15


@step(
    name="graphql_query",
    version="v1.0",
    description="GraphQL query executor",
    tags=["connectivity", "graphql", "api", "sync"]
)
class GraphQLQueryStep(BaseStep):
    """Step for executing GraphQL queries and mutations."""

    def __init__(
        self,
        response_key: str = "graphql_response",
        name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__()
        self.response_key = response_key
        self.name = name or "graphql_query"
        self.version = version

    @to_obj(GraphQLContext)
    def __call__(self, data: GraphQLContext) -> Dict[str, Any]:
        """Execute the GraphQL query/mutation.
        
        Args:
            data: Context containing url, query, variables, headers, timeout.
            
        Returns:
            Dictionary with operation result.
        """
        payload = {
            "query": data.query,
            "variables": data.variables or {}
        }
        
        try:
            response = requests.post(
                data.url,
                json=payload,
                headers=data.headers,
                timeout=data.timeout
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
