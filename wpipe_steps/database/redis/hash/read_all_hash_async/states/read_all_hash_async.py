"""
Redis hash operations - read_all_hash (asynchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.aio import RedisHashManager


class ReadAllHashContext(BaseModel):
    """Context for reading all fields from a Redis hash."""
    hash_name: str


@step(
    name="redis_hash_read_all_async",
    version="v1.0",
    description="Read all fields from a Redis hash (asynchronous)",
    tags=["redis", "hash", "read", "async"]
)
class RedisHashReadAllAsync(BaseStep):
    """Read all fields and values from a Redis hash (asynchronous)."""

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
        self.name = name or "redis_hash_read_all_async"
        self.version = version

    @to_obj(ReadAllHashContext)
    async def __call__(self, data: ReadAllHashContext) -> Dict[str, Any]:
        """Execute the read_all_hash operation on Redis hash asynchronously.

        Args:
            data: Context containing hash_name.

        Returns:
            Dictionary with operation result.
        """
        try:
            manager = RedisHashManager(host=self.host, port=self.port, db=self.db)
            result = await manager.read_all_hash(hash_name=data.hash_name)
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
