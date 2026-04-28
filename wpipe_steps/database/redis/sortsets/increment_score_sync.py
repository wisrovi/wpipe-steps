"""
Redis sorted set operations - increment_score (synchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.sync import RedisSortedSetManager


class IncrementScoreContext(BaseModel):
    """Context for incrementing score in a Redis sorted set."""
    key: str
    increment: float
    member: str


@step(
    name="redis_sortsets_increment_score_sync",
    version="v1.0",
    description="Increment score of member in Redis sorted set (synchronous)",
    tags=["redis", "sortsets", "update", "sync"]
)
class RedisSortsetsIncrementScoreSync(BaseStep):
    """Increment score of member in a Redis sorted set (synchronous)."""

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
        self.name = name or "redis_sortsets_increment_score_sync"
        self.version = version
        self.manager = RedisSortedSetManager(host=host, port=port, db=db)

    @to_obj(IncrementScoreContext)
    def __call__(self, data: IncrementScoreContext) -> Dict[str, Any]:
        """Execute the increment_score operation.

        Args:
            data: Context containing key, increment, and member.

        Returns:
            Dictionary with operation result.
        """
        try:
            result = self.manager.increment_score(
                key=data.key,
                increment=data.increment,
                member=data.member
            )
            return {
                "success": True,
                "operation": "increment_score",
                "key": data.key,
                "member": data.member,
                "new_score": result
            }
        except Exception as e:
            return {
                "success": False,
                "operation": "increment_score",
                "error": str(e)
            }
