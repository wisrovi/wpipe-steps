"""
Redis sorted set operations - add_to_sorted_set (synchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.sync import RedisSortedSetManager


class AddToSortedSetContext(BaseModel):
    """Context for adding to a Redis sorted set."""
    key: str
    score: float
    member: str
    ttl: int = -1


@step(
    name="redis_sortsets_add_sync",
    version="v1.0",
    description="Add member to Redis sorted set (synchronous)",
    tags=["redis", "sortsets", "write", "sync"]
)
class RedisSortsetsAddSync(BaseStep):
    """Add a member with score to a Redis sorted set (synchronous)."""

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
        self.name = name or "redis_sortsets_add_sync"
        self.version = version
        self.manager = RedisSortedSetManager(host=host, port=port, db=db)

    @to_obj(AddToSortedSetContext)
    def __call__(self, data: AddToSortedSetContext) -> Dict[str, Any]:
        """Execute the add_to_sorted_set operation.

        Args:
            data: Context containing key, score, member, and optional ttl.

        Returns:
            Dictionary with operation result.
        """
        try:
            self.manager.add_to_sorted_set(
                key=data.key,
                score=data.score,
                member=data.member,
                ttl=data.ttl
            )
            return {
                "success": True,
                "operation": "add_to_sorted_set",
                "key": data.key,
                "member": data.member
            }
        except Exception as e:
            return {
                "success": False,
                "operation": "add_to_sorted_set",
                "error": str(e)
            }
