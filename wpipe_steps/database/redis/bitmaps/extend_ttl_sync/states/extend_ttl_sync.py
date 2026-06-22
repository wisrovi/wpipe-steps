"""
Redis bitmap operations - extend_ttl (synchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.sync import RedisBitmapManager


class BitmapExtendTtlContext(BaseModel):
    """Context for extending TTL of a Redis bitmap key."""
    key: str
    ttl: int


@step(
    name="redis_bitmap_extend_ttl_sync",
    version="v1.0",
    description="Extend TTL of a Redis bitmap key (synchronous)",
    tags=["redis", "bitmap", "ttl", "sync"]
)
class RedisBitmapExtendTtlSync(BaseStep):
    """Extend TTL of a Redis bitmap key (synchronous)."""

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
        self.name = name or "redis_bitmap_extend_ttl_sync"
        self.version = version
        self.manager = RedisBitmapManager(host=host, port=port, db=db)

    @to_obj(BitmapExtendTtlContext)
    def __call__(self, data: BitmapExtendTtlContext) -> Dict[str, Any]:
        """Execute the extend_ttl operation on Redis bitmap.

        Args:
            data: Context containing key and ttl.

        Returns:
            Dictionary with operation result.
        """
        try:
            self.manager.extend_ttl(key=data.key, ttl=data.ttl)
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
