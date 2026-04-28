"""
Redis hash operations - create_hash (synchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.sync import RedisHashManager


class CreateHashContext(BaseModel):
    """Context for creating a hash field in Redis."""
    hash_name: str
    key: str
    value: Dict[str, Any]
    ttl: int = -1


@step(
    name="redis_hash_create_sync",
    version="v1.0",
    description="Create a hash field in Redis (synchronous)",
    tags=["redis", "hash", "write", "sync"]
)
class RedisHashCreateSync(BaseStep):
    """Create a hash field in Redis (synchronous)."""

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
        self.name = name or "redis_hash_create_sync"
        self.version = version
        self.manager = RedisHashManager(host=host, port=port, db=db)

    @to_obj(CreateHashContext)
    def __call__(self, data: CreateHashContext) -> Dict[str, Any]:
        """Execute the create_hash operation on Redis hash.

        Args:
            data: Context containing hash_name, key, value, and optional ttl.

        Returns:
            Dictionary with operation result.
        """
        try:
            self.manager.create_hash(
                hash_name=data.hash_name,
                key=data.key,
                value=data.value,
                ttl=data.ttl
            )
            return {
                "success": True,
                "operation": "create_hash",
                "hash_name": data.hash_name,
                "key": data.key
            }
        except Exception as e:
            return {
                "success": False,
                "operation": "create_hash",
                "error": str(e)
            }
