"""
Redis geo operations - get_positions (synchronous).
"""

from typing import Any, Dict, List, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.sync import RedisGeoManager


class GetPositionsContext(BaseModel):
    """Context for getting positions of members in Redis geo."""
    key: str
    members: List[str]


@step(
    name="redis_geo_get_positions_sync",
    version="v1.0",
    description="Get positions of members in Redis geo set (synchronous)",
    tags=["redis", "geo", "read", "sync"]
)
class RedisGeoGetPositionsSync(BaseStep):
    """Get positions of members in a Redis geo set (synchronous)."""

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
        self.name = name or "redis_geo_get_positions_sync"
        self.version = version
        self.manager = RedisGeoManager(host=host, port=port, db=db)

    @to_obj(GetPositionsContext)
    def __call__(self, data: GetPositionsContext) -> Dict[str, Any]:
        """Execute the get_positions operation.

        Args:
            data: Context containing key and members.

        Returns:
            Dictionary with operation result.
        """
        try:
            result = self.manager.get_positions(data.key, *data.members)
            return {
                "success": True,
                "operation": "get_positions",
                "key": data.key,
                "positions": result
            }
        except Exception as e:
            return {
                "success": False,
                "operation": "get_positions",
                "error": str(e)
            }
