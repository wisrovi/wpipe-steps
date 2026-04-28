"""
Redis queue operations - get_queue_length (asynchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.aio import RedisQueueManager


class QueueLengthContext(BaseModel):
    """Context for getting queue length."""
    queue_name: str


@step(
    name="redis_queue_get_length_async",
    version="v1.0",
    description="Get length of a Redis queue (asynchronous)",
    tags=["redis", "queue", "read", "async"]
)
class RedisQueueGetLengthAsync(BaseStep):
    """Get length of a Redis queue (asynchronous)."""

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
        self.name = name or "redis_queue_get_length_async"
        self.version = version

    @to_obj(QueueLengthContext)
    async def __call__(self, data: QueueLengthContext) -> Dict[str, Any]:
        """Execute the get_queue_length operation asynchronously.

        Args:
            data: Context containing queue_name.

        Returns:
            Dictionary with operation result.
        """
        try:
            manager = RedisQueueManager(host=self.host, port=self.port, db=self.db)
            result = await manager.get_queue_length(queue_name=data.queue_name)
            return {
                "success": True,
                "operation": "get_queue_length",
                "queue_name": data.queue_name,
                "length": result
            }
        except Exception as e:
            return {
                "success": False,
                "operation": "get_queue_length",
                "error": str(e)
            }
