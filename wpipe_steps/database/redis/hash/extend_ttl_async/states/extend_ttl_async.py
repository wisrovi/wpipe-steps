"""
Redis hash operations - extend_ttl (asynchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.aio import RedisHashManager


class HashExtendTtlContext(BaseModel):
    """Context for extending TTL of a Redis hash key."""
    hash_name: str
    ttl: int


@step(
    name="redis_hash_extend_ttl_async",
    version="v1.0",
    description="Extend TTL of a Redis hash key (asynchronous)",
    tags=["redis", "hash", "ttl", "async"]
)
class RedisHashExtendTtlAsync(BaseStep):
    """Extend TTL of a Redis hash key (asynchronous)."""

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
        self.name = name or "redis_hash_extend_ttl_async"
        self.version = version

    @to_obj(HashExtendTtlContext)
    async def __call__(self, data: HashExtendTtlContext) -> Dict[str, Any]:
        """Execute the extend_ttl operation on Redis hash asynchronously.

        Args:
            data: Context containing hash_name and ttl.

        Returns:
            Dictionary with operation result.
        """
        try:
            manager = RedisHashManager(host=self.host, port=self.port, db=self.db)
            await manager.extend_ttl(hash_name=data.hash_name, ttl=data.ttl)
            return {
                "success": True,
                "operation": "extend_ttl",
                "hash_name": data.hash_name,
                "ttl": data.ttl
            }
        except Exception as e:
            return {
                "success": False,
                "operation": "extend_ttl",
                "error": str(e)
            }
