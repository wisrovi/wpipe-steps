"""
Redis geo operations - get_distance (asynchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.aio import RedisGeoManager


class GetDistanceContext(BaseModel):
    """Context for getting distance between two members in Redis geo."""
    key: str
    member1: str
    member2: str
    unit: str = "km"


@step(
    name="redis_geo_get_distance_async",
    version="v1.0",
    description="Get distance between members in Redis geo set (asynchronous)",
    tags=["redis", "geo", "read", "async"]
)
class RedisGeoGetDistanceAsync(BaseStep):
    """Get distance between two members in a Redis geo set (asynchronous)."""

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
        self.name = name or "redis_geo_get_distance_async"
        self.version = version

    @to_obj(GetDistanceContext)
    async def __call__(self, data: GetDistanceContext) -> Dict[str, Any]:
        """Execute the get_distance operation asynchronously.

        Args:
            data: Context containing key, member1, member2, unit.

        Returns:
            Dictionary with operation result.
        """
        try:
            manager = RedisGeoManager(host=self.host, port=self.port, db=self.db)
            result = await manager.get_distance(
                key=data.key,
                member1=data.member1,
                member2=data.member2,
                unit=data.unit
            )
            return {
                "success": True,
                "operation": "get_distance",
                "key": data.key,
                "distance": result
            }
        except Exception as e:
            return {
                "success": False,
                "operation": "get_distance",
                "error": str(e)
            }
