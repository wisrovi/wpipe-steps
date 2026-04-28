"""
Redis stream operations - read_from_stream (asynchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.aio import RedisStreamManager


class ReadFromStreamContext(BaseModel):
    """Context for reading from a Redis stream."""
    key: str
    count: int = 1
    block: Optional[int] = None


@step(
    name="redis_stream_read_async",
    version="v1.0",
    description="Read messages from Redis stream (asynchronous)",
    tags=["redis", "streams", "read", "async"]
)
class RedisStreamReadAsync(BaseStep):
    """Read messages from a Redis stream (asynchronous)."""

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
        self.name = name or "redis_stream_read_async"
        self.version = version

    @to_obj(ReadFromStreamContext)
    async def __call__(self, data: ReadFromStreamContext) -> Dict[str, Any]:
        """Execute the read_from_stream operation asynchronously.

        Args:
            data: Context containing key, count, and optional block.

        Returns:
            Dictionary with operation result.
        """
        try:
            manager = RedisStreamManager(host=self.host, port=self.port, db=self.db)
            result = await manager.read_from_stream(
                key=data.key,
                count=data.count,
                block=data.block
            )
            return {
                "success": True,
                "operation": "read_from_stream",
                "key": data.key,
                "messages": result
            }
        except Exception as e:
            return {
                "success": False,
                "operation": "read_from_stream",
                "error": str(e)
            }
