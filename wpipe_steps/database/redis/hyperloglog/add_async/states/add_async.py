"""
Redis hyperloglog operations - add (asynchronous).
"""

from typing import Any, Dict, List, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.aio import RedisHyperLogLogManager


class HyperLogLogAddContext(BaseModel):
    """Context for adding to Redis HyperLogLog."""
    key: str
    values: List[Any]


@step(
    name="redis_hll_add_async",
    version="v1.0",
    description="Add elements to Redis HyperLogLog (asynchronous)",
    tags=["redis", "hyperloglog", "write", "async"]
)
class RedisHLLAddAsync(BaseStep):
    """Add elements to a Redis HyperLogLog (asynchronous)."""

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
        self.name = name or "redis_hll_add_async"
        self.version = version

    @to_obj(HyperLogLogAddContext)
    async def __call__(self, data: HyperLogLogAddContext) -> Dict[str, Any]:
        """Execute the add operation on Redis HyperLogLog asynchronously.

        Args:
            data: Context containing key and values.

        Returns:
            Dictionary with operation result.
        """
        try:
            manager = RedisHyperLogLogManager(host=self.host, port=self.port, db=self.db)
            await manager.add(data.key, *data.values)
            return {
                "success": True,
                "operation": "add",
                "key": data.key,
                "values": data.values
            }
        except Exception as e:
            return {
                "success": False,
                "operation": "add",
                "error": str(e)
            }
