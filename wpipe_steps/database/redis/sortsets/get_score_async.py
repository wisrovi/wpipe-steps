"""
Redis sorted set operations - get_score (asynchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.aio import RedisSortedSetManager


class GetScoreContext(BaseModel):
    """Context for getting score from a Redis sorted set."""
    key: str
    member: str


@step(
    name="redis_sortsets_get_score_async",
    version="v1.0",
    description="Get score of member in Redis sorted set (asynchronous)",
    tags=["redis", "sortsets", "read", "async"]
)
class RedisSortsetsGetScoreAsync(BaseStep):
    """Get score of member in a Redis sorted set (asynchronous)."""

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
        self.name = name or "redis_sortsets_get_score_async"
        self.version = version

    @to_obj(GetScoreContext)
    async def __call__(self, data: GetScoreContext) -> Dict[str, Any]:
        """Execute the get_score operation asynchronously.

        Args:
            data: Context containing key and member.

        Returns:
            Dictionary with operation result.
        """
        try:
            manager = RedisSortedSetManager(host=self.host, port=self.port, db=self.db)
            result = await manager.get_score(data.key, data.member)
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
