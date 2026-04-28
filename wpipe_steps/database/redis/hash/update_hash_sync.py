"""
Redis hash operations - update_hash (synchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.sync import RedisHashManager


class UpdateHashContext(BaseModel):
    """Context for updating a hash field in Redis."""
    hash_name: str
    key: str
    new_data: Dict[str, Any]


@step(
    name="redis_hash_update_sync",
    version="v1.0",
    description="Update a hash field in Redis (synchronous)",
    tags=["redis", "hash", "update", "sync"]
)
class RedisHashUpdateSync(BaseStep):
    """Update a hash field in Redis (synchronous)."""

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
        self.name = name or "redis_hash_update_sync"
        self.version = version
        self.manager = RedisHashManager(host=host, port=port, db=db)

    @to_obj(UpdateHashContext)
    def __call__(self, data: UpdateHashContext) -> Dict[str, Any]:
        """Execute the update_hash operation on Redis hash.

        Args:
            data: Context containing hash_name, key, and new_data.

        Returns:
            Dictionary with operation result.
        """
        try:
            self.manager.update_hash(
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
