"""
Redis sorted set operations - get_sorted_set_reverse (synchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.sync import RedisSortedSetManager


class GetSortedSetReverseContext(BaseModel):
    """Context for getting members from a Redis sorted set in reverse order."""
    key: str
    start: int = 0
    stop: int = -1
    with_scores: bool = False


@step(
    name="redis_sortsets_get_reverse_sync",
    version="v1.0",
    description="Get members from Redis sorted set in reverse order (synchronous)",
    tags=["redis", "sortsets", "read", "sync"]
)
class RedisSortsetsGetReverseSync(BaseStep):
    """Get members from a Redis sorted set in descending order (synchronous)."""

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
        self.name = name or "redis_sortsets_get_reverse_sync"
        self.version = version
        self.manager = RedisSortedSetManager(host=host, port=port, db=db)

    @to_obj(GetSortedSetReverseContext)
    def __call__(self, data: GetSortedSetReverseContext) -> Dict[str, Any]:
        """Execute the get_sorted_set_reverse operation.

        Args:
            data: Context containing key, start, stop, and with_scores.

        Returns:
            Dictionary with operation result.
        """
        try:
            result = self.manager.get_sorted_set_reverse(
                key=data.key,
                start=data.start,
                stop=data.stop,
                with_scores=data.with_scores
            )
            return {
                "success": True,
                "operation": "get_sorted_set_reverse",
                "key": data.key,
                "result": result
            }
        except Exception as e:
            return {
                "success": False,
                "operation": "get_sorted_set_reverse",
                "error": str(e)
            }
