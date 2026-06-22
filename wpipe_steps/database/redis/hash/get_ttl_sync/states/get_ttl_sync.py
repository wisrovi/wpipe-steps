"""
Redis hash operations - get_ttl (synchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.sync import RedisHashManager


class HashTtlContext(BaseModel):
    """Context for hash TTL operations."""
    hash_name: str


@step(
    name="redis_hash_get_ttl_sync",
    version="v1.0",
    description="Get TTL of a Redis hash key (synchronous)",
    tags=["redis", "hash", "ttl", "sync"]
)
class RedisHashGetTtlSync(BaseStep):
    """Get TTL of a Redis hash key (synchronous)."""

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
        self.name = name or "redis_hash_get_ttl_sync"
        self.version = version
        self.manager = RedisHashManager(host=host, port=port, db=db)

    @to_obj(HashTtlContext)
    def __call__(self, data: HashTtlContext) -> Dict[str, Any]:
        """Execute the get_ttl operation on Redis hash.

        Args:
            data: Context containing hash_name.

        Returns:
            Dictionary with operation result.
        """
        try:
            result = self.manager.get_ttl(hash_name=data.hash_name)
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
