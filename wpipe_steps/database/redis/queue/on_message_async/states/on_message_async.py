"""
Redis queue operations - on_message (asynchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.aio import RedisQueueManager


class QueueOnMessageContext(BaseModel):
    """Context for subscribing to a Redis queue."""
    queue_name: str


@step(
    name="redis_queue_on_message_async",
    version="v1.0",
    description="Subscribe to a Redis queue (asynchronous)",
    tags=["redis", "queue", "read", "async"]
)
class RedisQueueOnMessageAsync(BaseStep):
    """Subscribe to a Redis queue and register callback (asynchronous)."""

    def __init__(
        self,
        host: str = "192.168.1.84",
        port: int = 6379,
        db: int = 0,
        poll_interval: int = 1,
        name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__()
        self.host = host
        self.port = port
        self.db = db
        self.poll_interval = poll_interval
        self.name = name or "redis_queue_on_message_async"
        self.version = version

    @to_obj(QueueOnMessageContext)
    async def __call__(self, data: QueueOnMessageContext) -> Dict[str, Any]:
        """Subscribe to queue and get decorator asynchronously.

        Args:
            data: Context containing queue_name.

        Returns:
            Dictionary with operation result.
        """
        try:
            manager = RedisQueueManager(host=self.host, port=self.port, db=self.db, poll_interval=self.poll_interval)
            decorator = manager.on_message(data.queue_name)
            return {
                "success": True,
                "operation": "on_message",
                "queue_name": data.queue_name,
                "decorator": decorator
            }
        except Exception as e:
            return {
                "success": False,
                "operation": "on_message",
                "error": str(e)
            }
