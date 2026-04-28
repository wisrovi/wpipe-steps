"""
Redis hash operations - read_all_hash (synchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.sync import RedisHashManager


class ReadAllHashContext(BaseModel):
    """Context for reading all fields from a Redis hash."""
    hash_name: str


@step(
    name="redis_hash_read_all_sync",
    version="v1.0",
    description="Read all fields from a Redis hash (synchronous)",
    tags=["redis", "hash", "read", "sync"]
)
class RedisHashReadAllSync(BaseStep):
    """Read all fields and values from a Redis hash (synchronous)."""

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
        self.name = name or "redis_hash_read_all_sync"
        self.version = version
        self.manager = RedisHashManager(host=host, port=port, db=db)

    @to_obj(ReadAllHashContext)
    def __call__(self, data: ReadAllHashContext) -> Dict[str, Any]:
        """Execute the read_all_hash operation on Redis hash.

        Args:
            data: Context containing hash_name.

        Returns:
            Dictionary with operation result.
        """
        try:
            result = self.manager.read_all_hash(hash_name=data.hash_name)
            return {
                "success": True,
                "operation": "read_all_hash",
                "hash_name": data.hash_name,
                "value": result
            }
        except Exception as e:
            return {
                "success": False,
                "operation": "read_all_hash",
                "error": str(e)
            }
