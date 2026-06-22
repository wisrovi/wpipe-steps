"""
Redis sorted set operations - get_sorted_set_by_score (asynchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.aio import RedisSortedSetManager


class GetSortedSetByScoreContext(BaseModel):
    """Context for getting members by score range from a Redis sorted set."""
    key: str
    min_score: float
    max_score: float
    with_scores: bool = False


@step(
    name="redis_sortsets_get_by_score_async",
    version="v1.0",
    description="Get members by score range from Redis sorted set (asynchronous)",
    tags=["redis", "sortsets", "read", "async"]
)
class RedisSortsetsGetByScoreAsync(BaseStep):
    """Get members by score range from a Redis sorted set (asynchronous)."""

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
        self.name = name or "redis_sortsets_get_by_score_async"
        self.version = version

    @to_obj(GetSortedSetByScoreContext)
    async def __call__(self, data: GetSortedSetByScoreContext) -> Dict[str, Any]:
        """Execute the get_sorted_set_by_score operation asynchronously.

        Args:
            data: Context containing key, min_score, max_score, and with_scores.

        Returns:
            Dictionary with operation result.
        """
        try:
            manager = RedisSortedSetManager(host=self.host, port=self.port, db=self.db)
            result = await manager.get_sorted_set_by_score(
                key=data.key,
                min_score=data.min_score,
                max_score=data.max_score,
                with_scores=data.with_scores
            )
            return {
                "success": True,
                "operation": "get_sorted_set_by_score",
                "key": data.key,
                "result": result
            }
        except Exception as e:
            return {
                "success": False,
                "operation": "get_sorted_set_by_score",
                "error": str(e)
            }
