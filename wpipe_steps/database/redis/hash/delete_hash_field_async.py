"""
Redis hash operations - delete_hash_field (asynchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.aio import RedisHashManager


class DeleteHashFieldContext(BaseModel):
    """Context for deleting a hash field in Redis."""
    hash_name: str
    key: str


@step(
    name="redis_hash_delete_async",
    version="v1.0",
    description="Delete a hash field from Redis (asynchronous)",
    tags=["redis", "hash", "delete", "async"]
)
class RedisHashDeleteAsync(BaseStep):
    """Delete a hash field from Redis (asynchronous)."""

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
        self.name = name or "redis_hash_delete_async"
        self.version = version

    @to_obj(DeleteHashFieldContext)
    async def __call__(self, data: DeleteHashFieldContext) -> Dict[str, Any]:
        """Execute the delete_hash_field operation on Redis hash asynchronously.

        Args:
            data: Context containing hash_name and key.

        Returns:
            Dictionary with operation result.
        """
        try:
            manager = RedisHashManager(host=self.host, port=self.port, db=self.db)
            await manager.delete_hash_field(
                hash_name=data.hash_name,
                key=data.key
            )
            return {
                "success": True,
                "operation": "delete_hash_field",
                "hash_name": data.hash_name,
                "key": data.key
            }
        except Exception as e:
            return {
                "success": False,
                "operation": "delete_hash_field",
                "error": str(e)
            }
