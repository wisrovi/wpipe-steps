"""
Redis hash operations - update_hash (asynchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.aio import RedisHashManager


class UpdateHashContext(BaseModel):
    """Context for updating a hash field in Redis."""
    hash_name: str
    key: str
    new_data: Dict[str, Any]


@step(
    name="redis_hash_update_async",
    version="v1.0",
    description="Update a hash field in Redis (asynchronous)",
    tags=["redis", "hash", "update", "async"]
)
class RedisHashUpdateAsync(BaseStep):
    """Update a hash field in Redis (asynchronous)."""

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
        self.name = name or "redis_hash_update_async"
        self.version = version

    @to_obj(UpdateHashContext)
    async def __call__(self, data: UpdateHashContext) -> Dict[str, Any]:
        """Execute the update_hash operation on Redis hash asynchronously.

        Args:
            data: Context containing hash_name, key, and new_data.

        Returns:
            Dictionary with operation result.
        """
        try:
            manager = RedisHashManager(host=self.host, port=self.port, db=self.db)
            await manager.update_hash(
                hash_name=data.hash_name,
                key=data.key,
                new_data=data.new_data
            )
            return {
                "success": True,
                "operation": "update_hash",
                "hash_name": data.hash_name,
                "key": data.key
            }
        except Exception as e:
            return {
                "success": False,
                "operation": "update_hash",
                "error": str(e)
            }
