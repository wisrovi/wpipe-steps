"""
Redis bitmap operations - get_bit (asynchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.aio import RedisBitmapManager


class GetBitContext(BaseModel):
    """Context for getting a bit from Redis bitmap."""
    key: str
    offset: int


@step(
    name="redis_bitmap_get_bit_async",
    version="v1.0",
    description="Get a bit from Redis bitmap (asynchronous)",
    tags=["redis", "bitmap", "read", "async"]
)
class RedisBitmapGetBitAsync(BaseStep):
    """Get a bit value at a given offset in a Redis string key (asynchronous)."""

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
        self.name = name or "redis_bitmap_get_bit_async"
        self.version = version

    @to_obj(GetBitContext)
    async def __call__(self, data: GetBitContext) -> Dict[str, Any]:
        """Execute the get_bit operation on Redis bitmap asynchronously.

        Args:
            data: Context containing key and offset.

        Returns:
            Dictionary with operation result.
        """
        try:
            manager = RedisBitmapManager(host=self.host, port=self.port, db=self.db)
            result = await manager.get_bit(
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
