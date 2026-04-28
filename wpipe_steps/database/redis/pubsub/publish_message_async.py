"""
Redis pubsub operations - publish_message (asynchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.aio import RedisPubSubManager


class PublishMessageContext(BaseModel):
    """Context for publishing a message to a Redis channel."""
    channel: str
    message: Any


@step(
    name="redis_pubsub_publish_async",
    version="v1.0",
    description="Publish a message to a Redis channel (asynchronous)",
    tags=["redis", "pubsub", "write", "async"]
)
class RedisPubsubPublishAsync(BaseStep):
    """Publish a message to a Redis channel (asynchronous)."""

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
        self.name = name or "redis_pubsub_publish_async"
        self.version = version

    @to_obj(PublishMessageContext)
    async def __call__(self, data: PublishMessageContext) -> Dict[str, Any]:
        """Execute the publish_message operation asynchronously.

        Args:
            data: Context containing channel and message.

        Returns:
            Dictionary with operation result.
        """
        try:
            manager = RedisPubSubManager(host=self.host, port=self.port, db=self.db)
            await manager.publish_message(
                channel=data.channel,
                message=data.message
            )
            return {
                "success": True,
                "operation": "publish_message",
                "channel": data.channel
            }
        except Exception as e:
            return {
                "success": False,
                "operation": "publish_message",
                "error": str(e)
            }
