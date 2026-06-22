"""
Redis geo operations - search_nearby (asynchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.aio import RedisGeoManager


class SearchNearbyContext(BaseModel):
    """Context for searching nearby members in Redis geo."""
    key: str
    longitude: float
    latitude: float
    radius: float
    unit: str = "km"
    count: Optional[int] = None


@step(
    name="redis_geo_search_nearby_async",
    version="v1.0",
    description="Search nearby members in Redis geo set (asynchronous)",
    tags=["redis", "geo", "read", "async"]
)
class RedisGeoSearchNearbyAsync(BaseStep):
    """Search nearby members in a Redis geo set (asynchronous)."""

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
        self.name = name or "redis_geo_search_nearby_async"
        self.version = version

    @to_obj(SearchNearbyContext)
    async def __call__(self, data: SearchNearbyContext) -> Dict[str, Any]:
        """Execute the search_nearby operation asynchronously.

        Args:
            data: Context containing key, longitude, latitude, radius, unit, count.

        Returns:
            Dictionary with operation result.
        """
        try:
            manager = RedisGeoManager(host=self.host, port=self.port, db=self.db)
            result = await manager.search_nearby(
                key=data.key,
                longitude=data.longitude,
                latitude=data.latitude,
                radius=data.radius,
                unit=data.unit,
                count=data.count
            )
            return {
                "success": True,
                "operation": "search_nearby",
                "key": data.key,
                "members": result
            }
        except Exception as e:
            return {
                "success": False,
                "operation": "search_nearby",
                "error": str(e)
            }
