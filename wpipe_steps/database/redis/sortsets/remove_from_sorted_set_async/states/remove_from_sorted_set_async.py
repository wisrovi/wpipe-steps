"""
Redis sorted set operations - remove_from_sorted_set (asynchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.aio import RedisSortedSetManager


class RemoveFromSortedSetContext(BaseModel):
    """Context for removing a member from a Redis sorted set."""
    key: str
    member: str


@step(
    name="redis_sortsets_remove_async",
    version="v1.0",
    description="Remove member from Redis sorted set (asynchronous)",
    tags=["redis", "sortsets", "delete", "async"]
)
class RedisSortsetsRemoveAsync(BaseStep):
    """Remove a member from a Redis sorted set (asynchronous)."""

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
        self.name = name or "redis_sortsets_remove_async"
        self.version = version

    @to_obj(RemoveFromSortedSetContext)
    async def __call__(self, data: RemoveFromSortedSetContext) -> Dict[str, Any]:
        """Execute the remove_from_sorted_set operation asynchronously.

        Args:
            data: Context containing key and member.

        Returns:
            Dictionary with operation result.
        """
        try:
            manager = RedisSortedSetManager(host=self.host, port=self.port, db=self.db)
            await manager.remove_from_sorted_set(
                key=data.key,
                member=data.member
            )
            return {
                "success": True,
                "operation": "remove_from_sorted_set",
                "key": data.key,
                "member": data.member
            }
        except Exception as e:
            return {
                "success": False,
                "operation": "remove_from_sorted_set",
                "error": str(e)
            }
