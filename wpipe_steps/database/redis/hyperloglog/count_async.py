"""
Redis hyperloglog operations - count (asynchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.aio import RedisHyperLogLogManager


class HyperLogLogCountContext(BaseModel):
    """Context for counting in Redis HyperLogLog."""
    key: str


@step(
    name="redis_hll_count_async",
    version="v1.0",
    description="Count unique elements in Redis HyperLogLog (asynchronous)",
    tags=["redis", "hyperloglog", "read", "async"]
)
class RedisHLLCountAsync(BaseStep):
    """Count unique elements in a Redis HyperLogLog (asynchronous)."""

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
        self.name = name or "redis_hll_count_async"
        self.version = version

    @to_obj(HyperLogLogCountContext)
    async def __call__(self, data: HyperLogLogCountContext) -> Dict[str, Any]:
        """Execute the count operation on Redis HyperLogLog asynchronously.

        Args:
            data: Context containing key.

        Returns:
            Dictionary with operation result.
        """
        try:
            manager = RedisHyperLogLogManager(host=self.host, port=self.port, db=self.db)
            result = await manager.count(data.key)
            return {
                "success": True,
                "operation": "count",
                "key": data.key,
                "count": result
            }
        except Exception as e:
            return {
                "success": False,
                "operation": "count",
                "error": str(e)
            }
