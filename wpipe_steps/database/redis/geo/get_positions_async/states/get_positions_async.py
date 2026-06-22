"""
Redis geo operations - get_positions (asynchronous).
"""

from typing import Any, Dict, List, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.aio import RedisGeoManager


class GetPositionsContext(BaseModel):
    """Context for getting positions of members in Redis geo."""
    key: str
    members: List[str]


@step(
    name="redis_geo_get_positions_async",
    version="v1.0",
    description="Get positions of members in Redis geo set (asynchronous)",
    tags=["redis", "geo", "read", "async"]
)
class RedisGeoGetPositionsAsync(BaseStep):
    """Get positions of members in a Redis geo set (asynchronous)."""

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
        self.name = name or "redis_geo_get_positions_async"
        self.version = version

    @to_obj(GetPositionsContext)
    async def __call__(self, data: GetPositionsContext) -> Dict[str, Any]:
        """Execute the get_positions operation asynchronously.

        Args:
            data: Context containing key and members.

        Returns:
            Dictionary with operation result.
        """
        try:
            manager = RedisGeoManager(host=self.host, port=self.port, db=self.db)
            result = await manager.get_positions(data.key, *data.members)
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
