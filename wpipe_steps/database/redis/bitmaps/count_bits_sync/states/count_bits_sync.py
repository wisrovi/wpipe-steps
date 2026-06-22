"""
Redis bitmap operations - count_bits (synchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.sync import RedisBitmapManager


class CountBitsContext(BaseModel):
    """Context for counting bits in Redis bitmap."""
    key: str


@step(
    name="redis_bitmap_count_bits_sync",
    version="v1.0",
    description="Count bits in Redis bitmap (synchronous)",
    tags=["redis", "bitmap", "read", "sync"]
)
class RedisBitmapCountBitsSync(BaseStep):
    """Count set bits in a Redis string key (synchronous)."""

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
        self.name = name or "redis_bitmap_count_bits_sync"
        self.version = version
        self.manager = RedisBitmapManager(host=host, port=port, db=db)

    @to_obj(CountBitsContext)
    def __call__(self, data: CountBitsContext) -> Dict[str, Any]:
        """Execute the count_bits operation on Redis bitmap.

        Args:
            data: Context containing key.

        Returns:
            Dictionary with operation result.
        """
        try:
            result = self.manager.count_bits(key=data.key)
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
