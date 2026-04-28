"""
Redis hash operations - read_hash (asynchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.aio import RedisHashManager


class ReadHashContext(BaseModel):
    """Context for reading a hash field from Redis."""
    hash_name: str
    key: str


@step(
    name="redis_hash_read_async",
    version="v1.0",
    description="Read a hash field from Redis (asynchronous)",
    tags=["redis", "hash", "read", "async"]
)
class RedisHashReadAsync(BaseStep):
    """Read a hash field from Redis (asynchronous)."""

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
        self.name = name or "redis_hash_read_async"
        self.version = version

    @to_obj(ReadHashContext)
    async def __call__(self, data: ReadHashContext) -> Dict[str, Any]:
        """Execute the read_hash operation on Redis hash asynchronously.

        Args:
            data: Context containing hash_name and key.

        Returns:
            Dictionary with operation result.
        """
        try:
            manager = RedisHashManager(host=self.host, port=self.port, db=self.db)
            result = await manager.read_hash(
                hash_name=data.hash_name,
                key=data.key
            )
            return {
                "success": True,
                "operation": "read_hash",
                "hash_name": data.hash_name,
                "key": data.key,
                "value": result
            }
        except Exception as e:
            return {
                "success": False,
                "operation": "read_hash",
                "error": str(e)
            }
