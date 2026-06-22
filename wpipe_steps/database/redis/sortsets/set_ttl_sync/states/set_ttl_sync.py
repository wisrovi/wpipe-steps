"""
Redis sorted set operations - set_ttl (synchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.sync import RedisSortedSetManager


class SetTtlSortedSetContext(BaseModel):
    """Context for setting TTL of a Redis sorted set."""
    key: str
    ttl: int


@step(
    name="redis_sortsets_set_ttl_sync",
    version="v1.0",
    description="Set TTL of a Redis sorted set (synchronous)",
    tags=["redis", "sortsets", "ttl", "sync"]
)
class RedisSortsetsSetTtlSync(BaseStep):
    """Set TTL of a Redis sorted set (synchronous)."""

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
        self.name = name or "redis_sortsets_set_ttl_sync"
        self.version = version
        self.manager = RedisSortedSetManager(host=host, port=port, db=db)

    @to_obj(SetTtlSortedSetContext)
    def __call__(self, data: SetTtlSortedSetContext) -> Dict[str, Any]:
        """Execute the set_ttl operation.

        Args:
            data: Context containing key and ttl.

        Returns:
            Dictionary with operation result.
        """
        try:
            self.manager.set_ttl(key=data.key, ttl=data.ttl)
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
