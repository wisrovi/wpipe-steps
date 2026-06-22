"""
Redis stream operations - on_message (asynchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.aio import RedisStreamManager


class StreamOnMessageContext(BaseModel):
    """Context for consuming from a Redis stream."""
    stream_name: str
    group_name: str
    consumer_name: str


@step(
    name="redis_stream_on_message_async",
    version="v1.0",
    description="Consume messages from Redis stream (asynchronous)",
    tags=["redis", "streams", "read", "async"]
)
class RedisStreamOnMessageAsync(BaseStep):
    """Consume messages from a Redis stream with consumer group (asynchronous)."""

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
        self.name = name or "redis_stream_on_message_async"
        self.version = version

    @to_obj(StreamOnMessageContext)
    async def __call__(self, data: StreamOnMessageContext) -> Dict[str, Any]:
        """Subscribe to stream and get decorator asynchronously.

        Args:
            data: Context containing stream_name, group_name, consumer_name.

        Returns:
            Dictionary with operation result.
        """
        try:
            manager = RedisStreamManager(host=self.host, port=self.port, db=self.db)
            decorator = manager.on_message(
                stream_name=data.stream_name,
                group_name=data.group_name,
                consumer_name=data.consumer_name
            )
            return {
                "success": True,
                "operation": "on_message",
                "stream_name": data.stream_name,
                "decorator": decorator
            }
        except Exception as e:
            return {
                "success": False,
                "operation": "on_message",
                "error": str(e)
            }
