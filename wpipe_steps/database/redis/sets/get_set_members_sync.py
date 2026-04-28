"""
Redis set operations - get_set_members (synchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.sync import RedisSetManager


class GetSetMembersContext(BaseModel):
    """Context for getting members from a Redis set."""
    key: str


@step(
    name="redis_set_get_members_sync",
    version="v1.0",
    description="Get all members from a Redis set (synchronous)",
    tags=["redis", "set", "read", "sync"]
)
class RedisSetGetMembersSync(BaseStep):
    """Get all members from a Redis set (synchronous)."""

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
        self.name = name or "redis_set_get_members_sync"
        self.version = version
        self.manager = RedisSetManager(host=host, port=port, db=db)

    @to_obj(GetSetMembersContext)
    def __call__(self, data: GetSetMembersContext) -> Dict[str, Any]:
        """Execute the get_set_members operation.

        Args:
            data: Context containing key.

        Returns:
            Dictionary with operation result.
        """
        try:
            result = self.manager.get_set_members(data.key)
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
