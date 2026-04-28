"""
Redis geo operations - add_location (synchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.sync import RedisGeoManager


class AddLocationContext(BaseModel):
    """Context for adding a location to a Redis geo set."""
    key: str
    member: str
    longitude: float
    latitude: float


@step(
    name="redis_geo_add_sync",
    version="v1.0",
    description="Add location to Redis geo set (synchronous)",
    tags=["redis", "geo", "write", "sync"]
)
class RedisGeoAddSync(BaseStep):
    """Add a location to a Redis geo set (synchronous)."""

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
        self.name = name or "redis_geo_add_sync"
        self.version = version
        self.manager = RedisGeoManager(host=host, port=port, db=db)

    @to_obj(AddLocationContext)
    def __call__(self, data: AddLocationContext) -> Dict[str, Any]:
        """Execute the add_location operation.

        Args:
            data: Context containing key, member, longitude, latitude.

        Returns:
            Dictionary with operation result.
        """
        try:
            self.manager.add_location(
                key=data.key,
                member=data.member,
                longitude=data.longitude,
                latitude=data.latitude
            )
            return {
                "success": True,
                "operation": "add_location",
                "key": data.key,
                "member": data.member
            }
        except Exception as e:
            return {
                "success": False,
                "operation": "add_location",
                "error": str(e)
            }
