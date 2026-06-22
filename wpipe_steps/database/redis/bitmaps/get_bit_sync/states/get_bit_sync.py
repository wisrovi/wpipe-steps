"""
Redis bitmap operations - get_bit (synchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.sync import RedisBitmapManager


class GetBitContext(BaseModel):
    """Context for getting a bit from Redis bitmap."""
    key: str
    offset: int


@step(
    name="redis_bitmap_get_bit_sync",
    version="v1.0",
    description="Get a bit from Redis bitmap (synchronous)",
    tags=["redis", "bitmap", "read", "sync"]
)
class RedisBitmapGetBitSync(BaseStep):
    """Get a bit value at a given offset in a Redis string key (synchronous)."""

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
        self.name = name or "redis_bitmap_get_bit_sync"
        self.version = version
        self.manager = RedisBitmapManager(host=host, port=port, db=db)

    @to_obj(GetBitContext)
    def __call__(self, data: GetBitContext) -> Dict[str, Any]:
        """Execute the get_bit operation on Redis bitmap.

        Args:
            data: Context containing key and offset.

        Returns:
            Dictionary with operation result.
        """
        try:
            result = self.manager.get_bit(
                key=data.key,
                offset=data.offset
            )
            return {
                "success": True,
                "operation": "get_bit",
                "key": data.key,
                "offset": data.offset,
                "result": result
            }
        except Exception as e:
            return {
                "success": False,
                "operation": "get_bit",
                "error": str(e)
            }
