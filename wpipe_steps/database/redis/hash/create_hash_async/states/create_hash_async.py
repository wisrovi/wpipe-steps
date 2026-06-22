"""
Redis hash operations - create_hash (asynchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.aio import RedisHashManager


class CreateHashContext(BaseModel):
    """Context for creating a hash field in Redis."""
    hash_name: str
    key: str
    value: Dict[str, Any]
    ttl: int = -1


@step(
    name="redis_hash_create_async",
    version="v1.0",
    description="Create a hash field in Redis (asynchronous)",
    tags=["redis", "hash", "write", "async"]
)
class RedisHashCreateAsync(BaseStep):
    """Create a hash field in Redis (asynchronous)."""

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
        self.name = name or "redis_hash_create_async"
        self.version = version

    @to_obj(CreateHashContext)
    async def __call__(self, data: CreateHashContext) -> Dict[str, Any]:
        """Execute the create_hash operation on Redis hash asynchronously.

        Args:
            data: Context containing hash_name, key, value, and optional ttl.

        Returns:
            Dictionary with operation result.
        """
        try:
            manager = RedisHashManager(host=self.host, port=self.port, db=self.db)
            await manager.create_hash(
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
