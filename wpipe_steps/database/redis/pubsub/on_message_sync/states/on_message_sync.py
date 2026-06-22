"""
Redis pubsub operations - on_message (synchronous).
"""

from typing import Any, Callable, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.sync import RedisPubSubManager


class OnMessageContext(BaseModel):
    """Context for subscribing to a Redis channel."""
    channel: str


@step(
    name="redis_pubsub_on_message_sync",
    version="v1.0",
    description="Subscribe to a Redis channel (synchronous)",
    tags=["redis", "pubsub", "read", "sync"]
)
class RedisPubsubOnMessageSync(BaseStep):
    """Subscribe to a Redis channel and register callback (synchronous)."""

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
        self.name = name or "redis_pubsub_on_message_sync"
        self.version = version
        self.manager = RedisPubSubManager(host=host, port=port, db=db)

    @to_obj(OnMessageContext)
    def __call__(self, data: OnMessageContext) -> Dict[str, Any]:
        """Subscribe to channel and start listening.

        Args:
            data: Context containing channel.

        Returns:
            Dictionary with operation result.
        """
        try:
            # Note: This returns the decorator for user to apply to callback
            decorator = self.manager.on_message(data.channel)
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
