"""
Redis set operations - remove_from_set (asynchronous).
"""

from typing import Any, Dict, List, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.aio import RedisSetManager


class RemoveFromSetContext(BaseModel):
    """Context for removing members from a Redis set."""
    key: str
    values: List[Any]


@step(
    name="redis_set_remove_async",
    version="v1.0",
    description="Remove members from a Redis set (asynchronous)",
    tags=["redis", "set", "delete", "async"]
)
class RedisSetRemoveAsync(BaseStep):
    """Remove members from a Redis set (asynchronous)."""

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
        self.name = name or "redis_set_remove_async"
        self.version = version

    @to_obj(RemoveFromSetContext)
    async def __call__(self, data: RemoveFromSetContext) -> Dict[str, Any]:
        """Execute the remove_from_set operation asynchronously.

        Args:
            data: Context containing key and values.

        Returns:
            Dictionary with operation result.
        """
        try:
            manager = RedisSetManager(host=self.host, port=self.port, db=self.db)
            await manager.remove_from_set(data.key, *data.values)
            return {
                "success": True,
                "operation": "remove_from_set",
                "key": data.key,
                "values": data.values
            }
        except Exception as e:
            return {
                "success": False,
                "operation": "remove_from_set",
                "error": str(e)
            }
