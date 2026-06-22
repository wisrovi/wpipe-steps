"""
Redis sorted set operations - set_ttl (asynchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.aio import RedisSortedSetManager


class SetTtlSortedSetContext(BaseModel):
    """Context for setting TTL of a Redis sorted set."""
    key: str
    ttl: int


@step(
    name="redis_sortsets_set_ttl_async",
    version="v1.0",
    description="Set TTL of a Redis sorted set (asynchronous)",
    tags=["redis", "sortsets", "ttl", "async"]
)
class RedisSortsetsSetTtlAsync(BaseStep):
    """Set TTL of a Redis sorted set (asynchronous)."""

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
        self.name = name or "redis_sortsets_set_ttl_async"
        self.version = version

    @to_obj(SetTtlSortedSetContext)
    async def __call__(self, data: SetTtlSortedSetContext) -> Dict[str, Any]:
        """Execute the set_ttl operation asynchronously.

        Args:
            data: Context containing key and ttl.

        Returns:
            Dictionary with operation result.
        """
        try:
            manager = RedisSortedSetManager(host=self.host, port=self.port, db=self.db)
            await manager.set_ttl(key=data.key, ttl=data.ttl)
            return {
                "success": True,
                "operation": "set_ttl",
                "key": data.key,
                "ttl": data.ttl
            }
        except Exception as e:
            return {
                "success": False,
                "operation": "set_ttl",
                "error": str(e)
            }
