"""
Redis geo operations - search_nearby (synchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.sync import RedisGeoManager


class SearchNearbyContext(BaseModel):
    """Context for searching nearby members in Redis geo."""
    key: str
    longitude: float
    latitude: float
    radius: float
    unit: str = "km"
    count: Optional[int] = None


@step(
    name="redis_geo_search_nearby_sync",
    version="v1.0",
    description="Search nearby members in Redis geo set (synchronous)",
    tags=["redis", "geo", "read", "sync"]
)
class RedisGeoSearchNearbySync(BaseStep):
    """Search nearby members in a Redis geo set (synchronous)."""

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
        self.name = name or "redis_geo_search_nearby_sync"
        self.version = version
        self.manager = RedisGeoManager(host=host, port=port, db=db)

    @to_obj(SearchNearbyContext)
    def __call__(self, data: SearchNearbyContext) -> Dict[str, Any]:
        """Execute the search_nearby operation.

        Args:
            data: Context containing key, longitude, latitude, radius, unit, count.

        Returns:
            Dictionary with operation result.
        """
        try:
            result = self.manager.search_nearby(
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
