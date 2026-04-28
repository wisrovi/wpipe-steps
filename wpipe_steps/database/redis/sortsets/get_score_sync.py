"""
Redis sorted set operations - get_score (synchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.sync import RedisSortedSetManager


class GetScoreContext(BaseModel):
    """Context for getting score from a Redis sorted set."""
    key: str
    member: str


@step(
    name="redis_sortsets_get_score_sync",
    version="v1.0",
    description="Get score of member in Redis sorted set (synchronous)",
    tags=["redis", "sortsets", "read", "sync"]
)
class RedisSortsetsGetScoreSync(BaseStep):
    """Get score of member in a Redis sorted set (synchronous)."""

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
        self.name = name or "redis_sortsets_get_score_sync"
        self.version = version
        self.manager = RedisSortedSetManager(host=host, port=port, db=db)

    @to_obj(GetScoreContext)
    def __call__(self, data: GetScoreContext) -> Dict[str, Any]:
        """Execute the get_score operation.

        Args:
            data: Context containing key and member.

        Returns:
            Dictionary with operation result.
        """
        try:
            result = self.manager.get_score(data.key, data.member)
            return {
                "success": True,
                "operation": "get_score",
                "key": data.key,
                "member": data.member,
                "score": result
            }
        except Exception as e:
            return {
                "success": False,
                "operation": "get_score",
                "error": str(e)
            }
