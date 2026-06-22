"""
Redis set operations - get_set_members (asynchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.aio import RedisSetManager


class GetSetMembersContext(BaseModel):
    """Context for getting members from a Redis set."""
    key: str


@step(
    name="redis_set_get_members_async",
    version="v1.0",
    description="Get all members from a Redis set (asynchronous)",
    tags=["redis", "set", "read", "async"]
)
class RedisSetGetMembersAsync(BaseStep):
    """Get all members from a Redis set (asynchronous)."""

    def __init__(
        self,
        host: str = "192.168.1.84",
        port: int = 6379,
        db: int = 0,
        name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__()
        self.host = host
        self.port = port
        self.db = db
        self.name = name or "redis_set_get_members_async"
        self.version = version

    @to_obj(GetSetMembersContext)
    async def __call__(self, data: GetSetMembersContext) -> Dict[str, Any]:
        """Execute the get_set_members operation asynchronously.

        Args:
            data: Context containing key.

        Returns:
            Dictionary with operation result.
        """
        try:
            manager = RedisSetManager(host=self.host, port=self.port, db=self.db)
            result = await manager.get_set_members(data.key)
            return {
                "success": True,
                "operation": "get_set_members",
                "key": data.key,
                "members": result
            }
        except Exception as e:
            return {
                "success": False,
                "operation": "get_set_members",
                "error": str(e)
            }
