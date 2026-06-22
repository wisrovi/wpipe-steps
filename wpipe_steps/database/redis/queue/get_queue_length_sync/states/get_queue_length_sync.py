"""
Redis queue operations - get_queue_length (synchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.sync import RedisQueueManager


class QueueLengthContext(BaseModel):
    """Context for getting queue length."""
    queue_name: str


@step(
    name="redis_queue_get_length_sync",
    version="v1.0",
    description="Get length of a Redis queue (synchronous)",
    tags=["redis", "queue", "read", "sync"]
)
class RedisQueueGetLengthSync(BaseStep):
    """Get length of a Redis queue (synchronous)."""

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
        self.name = name or "redis_queue_get_length_sync"
        self.version = version
        self.manager = RedisQueueManager(host=host, port=port, db=db)

    @to_obj(QueueLengthContext)
    def __call__(self, data: QueueLengthContext) -> Dict[str, Any]:
        """Execute the get_queue_length operation.

        Args:
            data: Context containing queue_name.

        Returns:
            Dictionary with operation result.
        """
        try:
            result = self.manager.get_queue_length(queue_name=data.queue_name)
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
