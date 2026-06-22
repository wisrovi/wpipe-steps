"""
Redis geo operations - get_distance (synchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.sync import RedisGeoManager


class GetDistanceContext(BaseModel):
    """Context for getting distance between two members in Redis geo."""
    key: str
    member1: str
    member2: str
    unit: str = "km"


@step(
    name="redis_geo_get_distance_sync",
    version="v1.0",
    description="Get distance between members in Redis geo set (synchronous)",
    tags=["redis", "geo", "read", "sync"]
)
class RedisGeoGetDistanceSync(BaseStep):
    """Get distance between two members in a Redis geo set (synchronous)."""

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
        self.name = name or "redis_geo_get_distance_sync"
        self.version = version
        self.manager = RedisGeoManager(host=host, port=port, db=db)

    @to_obj(GetDistanceContext)
    def __call__(self, data: GetDistanceContext) -> Dict[str, Any]:
        """Execute the get_distance operation.

        Args:
            data: Context containing key, member1, member2, unit.

        Returns:
            Dictionary with operation result.
        """
        try:
            result = self.manager.get_distance(
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
