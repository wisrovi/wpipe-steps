"""
Redis bitmap operations - extend_ttl (asynchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.aio import RedisBitmapManager


class BitmapExtendTtlContext(BaseModel):
    """Context for extending TTL of a Redis bitmap key."""
    key: str
    ttl: int


@step(
    name="redis_bitmap_extend_ttl_async",
    version="v1.0",
    description="Extend TTL of a Redis bitmap key (asynchronous)",
    tags=["redis", "bitmap", "ttl", "async"]
)
class RedisBitmapExtendTtlAsync(BaseStep):
    """Extend TTL of a Redis bitmap key (asynchronous)."""

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
        self.name = name or "redis_bitmap_extend_ttl_async"
        self.version = version

    @to_obj(BitmapExtendTtlContext)
    async def __call__(self, data: BitmapExtendTtlContext) -> Dict[str, Any]:
        """Execute the extend_ttl operation on Redis bitmap asynchronously.

        Args:
            data: Context containing key and ttl.

        Returns:
            Dictionary with operation result.
        """
        try:
            manager = RedisBitmapManager(host=self.host, port=self.port, db=self.db)
            await manager.extend_ttl(key=data.key, ttl=data.ttl)
            return {
                "success": True,
                "operation": "extend_ttl",
                "key": data.key,
                "ttl": data.ttl
            }
        except Exception as e:
            return {
                "success": False,
                "operation": "extend_ttl",
                "error": str(e)
            }
