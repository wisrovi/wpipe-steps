"""
Redis set operations - remove_from_set (synchronous).
"""

from typing import Any, Dict, List, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.sync import RedisSetManager


class RemoveFromSetContext(BaseModel):
    """Context for removing members from a Redis set."""
    key: str
    values: List[Any]


@step(
    name="redis_set_remove_sync",
    version="v1.0",
    description="Remove members from a Redis set (synchronous)",
    tags=["redis", "set", "delete", "sync"]
)
class RedisSetRemoveSync(BaseStep):
    """Remove members from a Redis set (synchronous)."""

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
        self.name = name or "redis_set_remove_sync"
        self.version = version
        self.manager = RedisSetManager(host=host, port=port, db=db)

    @to_obj(RemoveFromSetContext)
    def __call__(self, data: RemoveFromSetContext) -> Dict[str, Any]:
        """Execute the remove_from_set operation.

        Args:
            data: Context containing key and values.

        Returns:
            Dictionary with operation result.
        """
        try:
            self.manager.remove_from_set(data.key, *data.values)
            return {
                "success": True,
                "operation": "remove_from_set",
                "key": data.key,
                "values": data.values
            }
        except Exception as e:
            return {
                "success": False,
                "operation": "remove_from_set",
                "error": str(e)
            }
