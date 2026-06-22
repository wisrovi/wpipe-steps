"""
Redis sorted set operations - remove_from_sorted_set (synchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.sync import RedisSortedSetManager


class RemoveFromSortedSetContext(BaseModel):
    """Context for removing a member from a Redis sorted set."""
    key: str
    member: str


@step(
    name="redis_sortsets_remove_sync",
    version="v1.0",
    description="Remove member from Redis sorted set (synchronous)",
    tags=["redis", "sortsets", "delete", "sync"]
)
class RedisSortsetsRemoveSync(BaseStep):
    """Remove a member from a Redis sorted set (synchronous)."""

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
        self.name = name or "redis_sortsets_remove_sync"
        self.version = version
        self.manager = RedisSortedSetManager(host=host, port=port, db=db)

    @to_obj(RemoveFromSortedSetContext)
    def __call__(self, data: RemoveFromSortedSetContext) -> Dict[str, Any]:
        """Execute the remove_from_sorted_set operation.

        Args:
            data: Context containing key and member.

        Returns:
            Dictionary with operation result.
        """
        try:
            self.manager.remove_from_sorted_set(
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
