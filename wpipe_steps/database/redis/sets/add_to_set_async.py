"""
Redis set operations - add_to_set (asynchronous).
"""

from typing import Any, Dict, List, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.aio import RedisSetManager


class AddToSetContext(BaseModel):
    """Context for adding members to a Redis set."""
    key: str
    values: List[Any]
    ttl: int = -1


@step(
    name="redis_set_add_async",
    version="v1.0",
    description="Add members to a Redis set (asynchronous)",
    tags=["redis", "set", "write", "async"]
)
class RedisSetAddAsync(BaseStep):
    """Add members to a Redis set (asynchronous)."""

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
        self.name = name or "redis_set_add_async"
        self.version = version

    @to_obj(AddToSetContext)
    async def __call__(self, data: AddToSetContext) -> Dict[str, Any]:
        """Execute the add_to_set operation asynchronously.

        Args:
            data: Context containing key, values, and optional ttl.

        Returns:
            Dictionary with operation result.
        """
        try:
            manager = RedisSetManager(host=self.host, port=self.port, db=self.db)
            await manager.add_to_set(data.key, *data.values, ttl=data.ttl)
            return {
                "success": True,
                "operation": "add_to_set",
                "key": data.key,
                "values": data.values
            }
        except Exception as e:
            return {
                "success": False,
                "operation": "add_to_set",
                "error": str(e)
            }
