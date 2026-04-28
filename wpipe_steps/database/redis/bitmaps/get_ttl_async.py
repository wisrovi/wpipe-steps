"""
Redis bitmap operations - get_ttl (asynchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.aio import RedisBitmapManager


class BitmapTtlContext(BaseModel):
    """Context for bitmap TTL operations."""
    key: str


@step(
    name="redis_bitmap_get_ttl_async",
    version="v1.0",
    description="Get TTL of a Redis bitmap key (asynchronous)",
    tags=["redis", "bitmap", "ttl", "async"]
)
class RedisBitmapGetTtlAsync(BaseStep):
    """Get TTL of a Redis bitmap key (asynchronous)."""

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
        self.name = name or "redis_bitmap_get_ttl_async"
        self.version = version

    @to_obj(BitmapTtlContext)
    async def __call__(self, data: BitmapTtlContext) -> Dict[str, Any]:
        """Execute the get_ttl operation on Redis bitmap asynchronously.

        Args:
            data: Context containing key.

        Returns:
            Dictionary with operation result.
        """
        try:
            manager = RedisBitmapManager(host=self.host, port=self.port, db=self.db)
            result = await manager.get_ttl(key=data.key)
            return {
                "success": True,
                "operation": "get_ttl",
                "key": data.key,
                "ttl": result
            }
        except Exception as e:
            return {
                "success": False,
                "operation": "get_ttl",
                "error": str(e)
            }
