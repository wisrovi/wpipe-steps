"""
Redis sorted set operations - delete_sorted_set (synchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.sync import RedisSortedSetManager


class DeleteSortedSetContext(BaseModel):
    """Context for deleting a Redis sorted set."""
    key: str


@step(
    name="redis_sortsets_delete_sync",
    version="v1.0",
    description="Delete a Redis sorted set (synchronous)",
    tags=["redis", "sortsets", "delete", "sync"]
)
class RedisSortsetsDeleteSync(BaseStep):
    """Delete a Redis sorted set (synchronous)."""

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
        self.name = name or "redis_sortsets_delete_sync"
        self.version = version
        self.manager = RedisSortedSetManager(host=host, port=port, db=db)

    @to_obj(DeleteSortedSetContext)
    def __call__(self, data: DeleteSortedSetContext) -> Dict[str, Any]:
        """Execute the delete_sorted_set operation.

        Args:
            data: Context containing key.

        Returns:
            Dictionary with operation result.
        """
        try:
            self.manager.delete_sorted_set(data.key)
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
