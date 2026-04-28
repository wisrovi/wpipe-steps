"""
Redis pubsub operations - on_message (asynchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.aio import RedisPubSubManager


class OnMessageContext(BaseModel):
    """Context for subscribing to a Redis channel."""
    channel: str


@step(
    name="redis_pubsub_on_message_async",
    version="v1.0",
    description="Subscribe to a Redis channel (asynchronous)",
    tags=["redis", "pubsub", "read", "async"]
)
class RedisPubsubOnMessageAsync(BaseStep):
    """Subscribe to a Redis channel and register callback (asynchronous)."""

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
        self.name = name or "redis_pubsub_on_message_async"
        self.version = version

    @to_obj(OnMessageContext)
    async def __call__(self, data: OnMessageContext) -> Dict[str, Any]:
        """Subscribe to channel and start listening asynchronously.

        Args:
            data: Context containing channel.

        Returns:
            Dictionary with operation result.
        """
        try:
            manager = RedisPubSubManager(host=self.host, port=self.port, db=self.db)
            decorator = manager.on_message(data.channel)
            return {
                "success": True,
                "operation": "on_message",
                "channel": data.channel,
                "decorator": decorator
            }
        except Exception as e:
            return {
                "success": False,
                "operation": "on_message",
                "error": str(e)
            }
