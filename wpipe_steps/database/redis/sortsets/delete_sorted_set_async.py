"""
Redis sorted set operations - delete_sorted_set (asynchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.aio import RedisSortedSetManager


class DeleteSortedSetContext(BaseModel):
    """Context for deleting a Redis sorted set."""
    key: str


@step(
    name="redis_sortsets_delete_async",
    version="v1.0",
    description="Delete a Redis sorted set (asynchronous)",
    tags=["redis", "sortsets", "delete", "async"]
)
class RedisSortsetsDeleteAsync(BaseStep):
    """Delete a Redis sorted set (asynchronous)."""

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
        self.name = name or "redis_sortsets_delete_async"
        self.version = version

    @to_obj(DeleteSortedSetContext)
    async def __call__(self, data: DeleteSortedSetContext) -> Dict[str, Any]:
        """Execute the delete_sorted_set operation asynchronously.

        Args:
            data: Context containing key.

        Returns:
            Dictionary with operation result.
        """
        try:
            manager = RedisSortedSetManager(host=self.host, port=self.port, db=self.db)
            await manager.delete_sorted_set(data.key)
            return {
                "success": True,
                "operation": "delete_sorted_set",
                "key": data.key
            }
        except Exception as e:
            return {
                "success": False,
                "operation": "delete_sorted_set",
                "error": str(e)
            }
