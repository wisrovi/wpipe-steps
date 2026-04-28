"""
Redis geo operations - add_location (asynchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.aio import RedisGeoManager


class AddLocationContext(BaseModel):
    """Context for adding a location to a Redis geo set."""
    key: str
    member: str
    longitude: float
    latitude: float


@step(
    name="redis_geo_add_async",
    version="v1.0",
    description="Add location to Redis geo set (asynchronous)",
    tags=["redis", "geo", "write", "async"]
)
class RedisGeoAddAsync(BaseStep):
    """Add a location to a Redis geo set (asynchronous)."""

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
        self.name = name or "redis_geo_add_async"
        self.version = version

    @to_obj(AddLocationContext)
    async def __call__(self, data: AddLocationContext) -> Dict[str, Any]:
        """Execute the add_location operation asynchronously.

        Args:
            data: Context containing key, member, longitude, latitude.

        Returns:
            Dictionary with operation result.
        """
        try:
            manager = RedisGeoManager(host=self.host, port=self.port, db=self.db)
            await manager.add_location(
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
