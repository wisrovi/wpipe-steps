"""
Redis geo operations - search_nearby_with_distance (synchronous).
"""

from typing import Any, Dict, List, Optional, Tuple
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.sync import RedisGeoManager


class SearchNearbyWithDistanceContext(BaseModel):
    """Context for searching nearby members with distance in Redis geo."""
    key: str
    longitude: float
    latitude: float
    radius: float
    unit: str = "km"


@step(
    name="redis_geo_search_nearby_dist_sync",
    version="v1.0",
    description="Search nearby members with distance in Redis geo set (synchronous)",
    tags=["redis", "geo", "read", "sync"]
)
class RedisGeoSearchNearbyDistSync(BaseStep):
    """Search nearby members with distance in a Redis geo set (synchronous)."""

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
        self.name = name or "redis_geo_search_nearby_dist_sync"
        self.version = version
        self.manager = RedisGeoManager(host=host, port=port, db=db)

    @to_obj(SearchNearbyWithDistanceContext)
    def __call__(self, data: SearchNearbyWithDistanceContext) -> Dict[str, Any]:
        """Execute the search_nearby_with_distance operation.

        Args:
            data: Context containing key, longitude, latitude, radius, unit.

        Returns:
            Dictionary with operation result.
        """
        try:
            result = self.manager.search_nearby_with_distance(
                key=data.key,
                longitude=data.longitude,
                latitude=data.latitude,
                radius=data.radius,
                unit=data.unit
            )
            return {
                "success": True,
                "operation": "search_nearby_with_distance",
                "key": data.key,
                "members_with_distance": result
            }
        except Exception as e:
            return {
                "success": False,
                "operation": "search_nearby_with_distance",
                "error": str(e)
            }
