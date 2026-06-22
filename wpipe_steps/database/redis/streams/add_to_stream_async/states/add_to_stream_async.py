"""
Redis stream operations - add_to_stream (asynchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.aio import RedisStreamManager


class AddToStreamContext(BaseModel):
    """Context for adding to a Redis stream."""
    key: str
    data: Dict[str, Any]
    ttl: Optional[int] = None


@step(
    name="redis_stream_add_async",
    version="v1.0",
    description="Add message to Redis stream (asynchronous)",
    tags=["redis", "streams", "write", "async"]
)
class RedisStreamAddAsync(BaseStep):
    """Add a message to a Redis stream (asynchronous)."""

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
        self.name = name or "redis_stream_add_async"
        self.version = version

    @to_obj(AddToStreamContext)
    async def __call__(self, data: AddToStreamContext) -> Dict[str, Any]:
        """Execute the add_to_stream operation asynchronously.

        Args:
            data: Context containing key, data, and optional ttl.

        Returns:
            Dictionary with operation result.
        """
        try:
            manager = RedisStreamManager(host=self.host, port=self.port, db=self.db)
            result = await manager.add_to_stream(
                key=data.key,
                data=data.data,
                ttl=data.ttl
            )
            return {
                "success": True,
                "operation": "add_to_stream",
                "key": data.key,
                "message_id": result
            }
        except Exception as e:
            return {
                "success": False,
                "operation": "add_to_stream",
                "error": str(e)
            }
