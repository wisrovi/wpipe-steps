"""
Redis sorted set operations - get_sorted_set_by_score (synchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.sync import RedisSortedSetManager


class GetSortedSetByScoreContext(BaseModel):
    """Context for getting members by score range from a Redis sorted set."""
    key: str
    min_score: float
    max_score: float
    with_scores: bool = False


@step(
    name="redis_sortsets_get_by_score_sync",
    version="v1.0",
    description="Get members by score range from Redis sorted set (synchronous)",
    tags=["redis", "sortsets", "read", "sync"]
)
class RedisSortsetsGetByScoreSync(BaseStep):
    """Get members by score range from a Redis sorted set (synchronous)."""

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
        self.name = name or "redis_sortsets_get_by_score_sync"
        self.version = version
        self.manager = RedisSortedSetManager(host=host, port=port, db=db)

    @to_obj(GetSortedSetByScoreContext)
    def __call__(self, data: GetSortedSetByScoreContext) -> Dict[str, Any]:
        """Execute the get_sorted_set_by_score operation.

        Args:
            data: Context containing key, min_score, max_score, and with_scores.

        Returns:
            Dictionary with operation result.
        """
        try:
            result = self.manager.get_sorted_set_by_score(
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
