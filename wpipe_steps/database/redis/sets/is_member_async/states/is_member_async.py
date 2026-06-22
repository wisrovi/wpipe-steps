"""
Redis set operations - is_member (asynchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.aio import RedisSetManager


class IsMemberContext(BaseModel):
    """Context for checking membership in a Redis set."""
    key: str
    value: Any


@step(
    name="redis_set_is_member_async",
    version="v1.0",
    description="Check if member exists in Redis set (asynchronous)",
    tags=["redis", "set", "read", "async"]
)
class RedisSetIsMemberAsync(BaseStep):
    """Check if a member exists in a Redis set (asynchronous)."""

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
        self.name = name or "redis_set_is_member_async"
        self.version = version

    @to_obj(IsMemberContext)
    async def __call__(self, data: IsMemberContext) -> Dict[str, Any]:
        """Execute the is_member operation asynchronously.

        Args:
            data: Context containing key and value.

        Returns:
            Dictionary with operation result.
        """
        try:
            manager = RedisSetManager(host=self.host, port=self.port, db=self.db)
            result = await manager.is_member(data.key, data.value)
            return {
                "success": True,
                "operation": "is_member",
                "key": data.key,
                "value": data.value,
                "is_member": result
            }
        except Exception as e:
            return {
                "success": False,
                "operation": "is_member",
                "error": str(e)
            }
