"""
Redis hash operations - extend_ttl (synchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.sync import RedisHashManager


class HashExtendTtlContext(BaseModel):
    """Context for extending TTL of a Redis hash key."""
    hash_name: str
    ttl: int


@step(
    name="redis_hash_extend_ttl_sync",
    version="v1.0",
    description="Extend TTL of a Redis hash key (synchronous)",
    tags=["redis", "hash", "ttl", "sync"]
)
class RedisHashExtendTtlSync(BaseStep):
    """Extend TTL of a Redis hash key (synchronous)."""

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
        self.name = name or "redis_hash_extend_ttl_sync"
        self.version = version
        self.manager = RedisHashManager(host=host, port=port, db=db)

    @to_obj(HashExtendTtlContext)
    def __call__(self, data: HashExtendTtlContext) -> Dict[str, Any]:
        """Execute the extend_ttl operation on Redis hash.

        Args:
            data: Context containing hash_name and ttl.

        Returns:
            Dictionary with operation result.
        """
        try:
            self.manager.extend_ttl(hash_name=data.hash_name, ttl=data.ttl)
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
