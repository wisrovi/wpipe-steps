"""
Redis hyperloglog operations - count (synchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.sync import RedisHyperLogLogManager


class HyperLogLogCountContext(BaseModel):
    """Context for counting in Redis HyperLogLog."""
    key: str


@step(
    name="redis_hll_count_sync",
    version="v1.0",
    description="Count unique elements in Redis HyperLogLog (synchronous)",
    tags=["redis", "hyperloglog", "read", "sync"]
)
class RedisHLLCountSync(BaseStep):
    """Count unique elements in a Redis HyperLogLog (synchronous)."""

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
        self.name = name or "redis_hll_count_sync"
        self.version = version
        self.manager = RedisHyperLogLogManager(host=host, port=port, db=db)

    @to_obj(HyperLogLogCountContext)
    def __call__(self, data: HyperLogLogCountContext) -> Dict[str, Any]:
        """Execute the count operation on Redis HyperLogLog.

        Args:
            data: Context containing key.

        Returns:
            Dictionary with operation result.
        """
        try:
            result = self.manager.count(data.key)
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
