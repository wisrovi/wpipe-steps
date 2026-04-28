"""
Redis sorted set operations - get_sorted_set (asynchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.aio import RedisSortedSetManager


class GetSortedSetContext(BaseModel):
    """Context for getting members from a Redis sorted set."""
    key: str
    start: int = 0
    stop: int = -1
    with_scores: bool = False


@step(
    name="redis_sortsets_get_async",
    version="v1.0",
    description="Get members from Redis sorted set (asynchronous)",
    tags=["redis", "sortsets", "read", "async"]
)
class RedisSortsetsGetAsync(BaseStep):
    """Get members from a Redis sorted set in ascending order (asynchronous)."""

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
        self.name = name or "redis_sortsets_get_async"
        self.version = version

    @to_obj(GetSortedSetContext)
    async def __call__(self, data: GetSortedSetContext) -> Dict[str, Any]:
        """Execute the get_sorted_set operation asynchronously.

        Args:
            data: Context containing key, start, stop, and with_scores.

        Returns:
            Dictionary with operation result.
        """
        try:
            manager = RedisSortedSetManager(host=self.host, port=self.port, db=self.db)
            result = await manager.get_sorted_set(
                key=data.key,
                start=data.start,
                stop=data.stop,
                with_scores=data.with_scores
            )
            return {
                "success": True,
                "operation": "get_sorted_set",
                "key": data.key,
                "result": result
            }
        except Exception as e:
            return {
                "success": False,
                "operation": "get_sorted_set",
                "error": str(e)
            }
