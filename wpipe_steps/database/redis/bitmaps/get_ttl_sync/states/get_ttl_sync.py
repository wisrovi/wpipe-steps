"""
Redis bitmap operations - get_ttl (synchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.sync import RedisBitmapManager


class BitmapTtlContext(BaseModel):
    """Context for bitmap TTL operations."""
    key: str


@step(
    name="redis_bitmap_get_ttl_sync",
    version="v1.0",
    description="Get TTL of a Redis bitmap key (synchronous)",
    tags=["redis", "bitmap", "ttl", "sync"]
)
class RedisBitmapGetTtlSync(BaseStep):
    """Get TTL of a Redis bitmap key (synchronous)."""

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
        self.name = name or "redis_bitmap_get_ttl_sync"
        self.version = version
        self.manager = RedisBitmapManager(host=host, port=port, db=db)

    @to_obj(BitmapTtlContext)
    def __call__(self, data: BitmapTtlContext) -> Dict[str, Any]:
        """Execute the get_ttl operation on Redis bitmap.

        Args:
            data: Context containing key.

        Returns:
            Dictionary with operation result.
        """
        try:
            result = self.manager.get_ttl(key=data.key)
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
