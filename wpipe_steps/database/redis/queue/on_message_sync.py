"""
Redis queue operations - on_message (synchronous).
"""

from typing import Any, Callable, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.sync import RedisQueueManager


class QueueOnMessageContext(BaseModel):
    """Context for subscribing to a Redis queue."""
    queue_name: str


@step(
    name="redis_queue_on_message_sync",
    version="v1.0",
    description="Subscribe to a Redis queue (synchronous)",
    tags=["redis", "queue", "read", "sync"]
)
class RedisQueueOnMessageSync(BaseStep):
    """Subscribe to a Redis queue and register callback (synchronous)."""

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
        self.name = name or "redis_queue_on_message_sync"
        self.version = version
        self.manager = RedisQueueManager(host=host, port=port, db=db, poll_interval=poll_interval)

    @to_obj(QueueOnMessageContext)
    def __call__(self, data: QueueOnMessageContext) -> Dict[str, Any]:
        """Subscribe to queue and get decorator for callback.

        Args:
            data: Context containing queue_name.

        Returns:
            Dictionary with operation result.
        """
        try:
            decorator = self.manager.on_message(data.queue_name)
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
