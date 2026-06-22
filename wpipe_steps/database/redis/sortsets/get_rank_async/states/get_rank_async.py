"""
Redis sorted set operations - get_rank (asynchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.aio import RedisSortedSetManager


class GetRankContext(BaseModel):
    """Context for getting rank from a Redis sorted set."""
    key: str
    member: str


@step(
    name="redis_sortsets_get_rank_async",
    version="v1.0",
    description="Get rank of member in Redis sorted set (asynchronous)",
    tags=["redis", "sortsets", "read", "async"]
)
class RedisSortsetsGetRankAsync(BaseStep):
    """Get rank of member in a Redis sorted set (asynchronous)."""

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
        self.name = name or "redis_sortsets_get_rank_async"
        self.version = version

    @to_obj(GetRankContext)
    async def __call__(self, data: GetRankContext) -> Dict[str, Any]:
        """Execute the get_rank operation asynchronously.

        Args:
            data: Context containing key and member.

        Returns:
            Dictionary with operation result.
        """
        try:
            manager = RedisSortedSetManager(host=self.host, port=self.port, db=self.db)
            result = await manager.get_rank(data.key, data.member)
            return {
                "success": True,
                "operation": "get_rank",
                "key": data.key,
                "member": data.member,
                "rank": result
            }
        except Exception as e:
            return {
                "success": False,
                "operation": "get_rank",
                "error": str(e)
            }
