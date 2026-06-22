"""
Redis hash operations - read_hash (synchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.sync import RedisHashManager


class ReadHashContext(BaseModel):
    """Context for reading a hash field from Redis."""
    hash_name: str
    key: str


@step(
    name="redis_hash_read_sync",
    version="v1.0",
    description="Read a hash field from Redis (synchronous)",
    tags=["redis", "hash", "read", "sync"]
)
class RedisHashReadSync(BaseStep):
    """Read a hash field from Redis (synchronous)."""

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
        self.name = name or "redis_hash_read_sync"
        self.version = version
        self.manager = RedisHashManager(host=host, port=port, db=db)

    @to_obj(ReadHashContext)
    def __call__(self, data: ReadHashContext) -> Dict[str, Any]:
        """Execute the read_hash operation on Redis hash.

        Args:
            data: Context containing hash_name and key.

        Returns:
            Dictionary with operation result.
        """
        try:
            result = self.manager.read_hash(
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
