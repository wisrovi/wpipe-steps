"""
Redis hash operations - get_ttl (asynchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.aio import RedisHashManager


class HashTtlContext(BaseModel):
    """Context for hash TTL operations."""
    hash_name: str


@step(
    name="redis_hash_get_ttl_async",
    version="v1.0",
    description="Get TTL of a Redis hash key (asynchronous)",
    tags=["redis", "hash", "ttl", "async"]
)
class RedisHashGetTtlAsync(BaseStep):
    """Get TTL of a Redis hash key (asynchronous)."""

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
        self.name = name or "redis_hash_get_ttl_async"
        self.version = version

    @to_obj(HashTtlContext)
    async def __call__(self, data: HashTtlContext) -> Dict[str, Any]:
        """Execute the get_ttl operation on Redis hash asynchronously.

        Args:
            data: Context containing hash_name.

        Returns:
            Dictionary with operation result.
        """
        try:
            manager = RedisHashManager(host=self.host, port=self.port, db=self.db)
            result = await manager.get_ttl(hash_name=data.hash_name)
            return {
                "success": True,
                "operation": "get_ttl",
                "hash_name": data.hash_name,
                "ttl": result
            }
        except Exception as e:
            return {
                "success": False,
                "operation": "get_ttl",
                "error": str(e)
            }
