"""
Redis sorted sets operations - get_ttl (synchronous).
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep


class GetTtlContext(BaseModel):
    """Context for getting TTL of a Redis key."""
    key: str


class RedisSortedSetGetTtlSync(BaseStep):
    """
    Get time to live for a Redis sorted set key (synchronous).
    
    Args:
        host: Redis host address.
        port: Redis port.
        db: Redis database number.
        name: Step name.
        version: Step version.
    """

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
        self.name = name or "redis_sorted_set_get_ttl_sync"
        self.version = version

    @step(name="redis_sorted_set_get_ttl_sync", version="v1.0", description="Get TTL for Redis sorted set key (sync)", tags=["redis", "sortsets", "read", "sync"])
    @to_obj(GetTtlContext)
    def __call__(self, context: GetTtlContext) -> Dict[str, Any]:
        """
        Execute the get_ttl operation on Redis sorted set.
        
        Args:
            context: Context containing key.
            
        Returns:
            Dictionary with operation result.
        """
        wredis = self.ensure_dependency("wredis")
        
        from wredis import sync as wredis_sync
        
        result = wredis_sync.get_ttl(
            key=context.key,
            host=self.host,
            port=self.port,
            db=self.db
        )
        
        return {"success": True, "operation": "get_ttl", "key": context.key, "result": result}
