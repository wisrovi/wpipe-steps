"""
Redis bitmap operations - set_bit (asynchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.aio import RedisBitmapManager


class SetBitContext(BaseModel):
    """Context for setting a bit in Redis bitmap."""
    key: str
    offset: int
    value: int
    ttl: int = -1


@step(
    name="redis_bitmap_set_bit_async",
    version="v1.0",
    description="Set a bit in Redis bitmap (asynchronous)",
    tags=["redis", "bitmap", "write", "async"]
)
class RedisBitmapSetBitAsync(BaseStep):
    """Set a bit value at a given offset in a Redis string key (asynchronous)."""

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
        self.name = name or "redis_bitmap_set_bit_async"
        self.version = version

    @to_obj(SetBitContext)
    async def __call__(self, data: SetBitContext) -> Dict[str, Any]:
        """Execute the set_bit operation on Redis bitmap asynchronously.

        Args:
            data: Context containing key, offset, value, and optional ttl.

        Returns:
            Dictionary with operation result.
        """
        try:
            manager = RedisBitmapManager(host=self.host, port=self.port, db=self.db)
            await manager.set_bit(
                key=data.key,
                offset=data.offset,
                value=data.value,
                ttl=data.ttl
            )
            return {
                "success": True,
                "operation": "set_bit",
                "key": data.key,
                "offset": data.offset,
                "value": data.value
            }
        except Exception as e:
            return {
                "success": False,
                "operation": "set_bit",
                "error": str(e)
            }
