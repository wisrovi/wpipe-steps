"""
Redis queue operations - publish (asynchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.aio import RedisQueueManager


class QueuePublishContext(BaseModel):
    """Context for publishing to a Redis queue."""
    queue_name: str
    data: Dict[str, Any]
    ttl: int = -1


@step(
    name="redis_queue_publish_async",
    version="v1.0",
    description="Publish a message to a Redis queue (asynchronous)",
    tags=["redis", "queue", "write", "async"]
)
class RedisQueuePublishAsync(BaseStep):
    """Publish a message to a Redis queue (asynchronous)."""

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
        self.name = name or "redis_queue_publish_async"
        self.version = version

    @to_obj(QueuePublishContext)
    async def __call__(self, data: QueuePublishContext) -> Dict[str, Any]:
        """Execute the publish operation on Redis queue asynchronously.

        Args:
            data: Context containing queue_name, data, and optional ttl.

        Returns:
            Dictionary with operation result.
        """
        try:
            manager = RedisQueueManager(host=self.host, port=self.port, db=self.db)
            await manager.publish(
                queue_name=data.queue_name,
                data=data.data,
                ttl=data.ttl
            )
            return {
                "success": True,
                "operation": "publish",
                "queue_name": data.queue_name
            }
        except Exception as e:
            return {
                "success": False,
                "operation": "publish",
                "error": str(e)
            }
