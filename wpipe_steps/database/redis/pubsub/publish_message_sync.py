"""
Redis pubsub operations - publish_message (synchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.sync import RedisPubSubManager


class PublishMessageContext(BaseModel):
    """Context for publishing a message to a Redis channel."""
    channel: str
    message: Any


@step(
    name="redis_pubsub_publish_sync",
    version="v1.0",
    description="Publish a message to a Redis channel (synchronous)",
    tags=["redis", "pubsub", "write", "sync"]
)
class RedisPubsubPublishSync(BaseStep):
    """Publish a message to a Redis channel (synchronous)."""

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
        self.name = name or "redis_pubsub_publish_sync"
        self.version = version
        self.manager = RedisPubSubManager(host=host, port=port, db=db)

    @to_obj(PublishMessageContext)
    def __call__(self, data: PublishMessageContext) -> Dict[str, Any]:
        """Execute the publish_message operation.

        Args:
            data: Context containing channel and message.

        Returns:
            Dictionary with operation result.
        """
        try:
            self.manager.publish_message(
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
