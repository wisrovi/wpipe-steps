"""
Redis hyperloglog operations - add (synchronous).
"""

from typing import Any, Dict, List, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.sync import RedisHyperLogLogManager


class HyperLogLogAddContext(BaseModel):
    """Context for adding to Redis HyperLogLog."""
    key: str
    values: List[Any]


@step(
    name="redis_hll_add_sync",
    version="v1.0",
    description="Add elements to Redis HyperLogLog (synchronous)",
    tags=["redis", "hyperloglog", "write", "sync"]
)
class RedisHLLAddSync(BaseStep):
    """Add elements to a Redis HyperLogLog (synchronous)."""

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
        self.name = name or "redis_hll_add_sync"
        self.version = version
        self.manager = RedisHyperLogLogManager(host=host, port=port, db=db)

    @to_obj(HyperLogLogAddContext)
    def __call__(self, data: HyperLogLogAddContext) -> Dict[str, Any]:
        """Execute the add operation on Redis HyperLogLog.

        Args:
            data: Context containing key and values.

        Returns:
            Dictionary with operation result.
        """
        try:
            self.manager.add(data.key, *data.values)
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
