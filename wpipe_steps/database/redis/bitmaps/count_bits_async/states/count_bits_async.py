"""
Redis bitmap operations - count_bits (asynchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.aio import RedisBitmapManager


class CountBitsContext(BaseModel):
    """Context for counting bits in Redis bitmap."""
    key: str


@step(
    name="redis_bitmap_count_bits_async",
    version="v1.0",
    description="Count bits in Redis bitmap (asynchronous)",
    tags=["redis", "bitmap", "read", "async"]
)
class RedisBitmapCountBitsAsync(BaseStep):
    """Count set bits in a Redis string key (asynchronous)."""

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
        self.name = name or "redis_bitmap_count_bits_async"
        self.version = version

    @to_obj(CountBitsContext)
    async def __call__(self, data: CountBitsContext) -> Dict[str, Any]:
        """Execute the count_bits operation on Redis bitmap asynchronously.

        Args:
            data: Context containing key.

        Returns:
            Dictionary with operation result.
        """
        try:
            manager = RedisBitmapManager(host=self.host, port=self.port, db=self.db)
            result = await manager.count_bits(key=data.key)
            return {
                "success": True,
                "operation": "count_bits",
                "key": data.key,
                "result": result
            }
        except Exception as e:
            return {
                "success": False,
                "operation": "count_bits",
                "error": str(e)
            }
