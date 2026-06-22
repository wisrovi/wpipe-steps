"""
Redis hash operations - delete_hash_field (synchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.sync import RedisHashManager


class DeleteHashFieldContext(BaseModel):
    """Context for deleting a hash field in Redis."""
    hash_name: str
    key: str


@step(
    name="redis_hash_delete_sync",
    version="v1.0",
    description="Delete a hash field from Redis (synchronous)",
    tags=["redis", "hash", "delete", "sync"]
)
class RedisHashDeleteSync(BaseStep):
    """Delete a hash field from Redis (synchronous)."""

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
        self.name = name or "redis_hash_delete_sync"
        self.version = version
        self.manager = RedisHashManager(host=host, port=port, db=db)

    @to_obj(DeleteHashFieldContext)
    def __call__(self, data: DeleteHashFieldContext) -> Dict[str, Any]:
        """Execute the delete_hash_field operation on Redis hash.

        Args:
            data: Context containing hash_name and key.

        Returns:
            Dictionary with operation result.
        """
        try:
            self.manager.delete_hash_field(
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
