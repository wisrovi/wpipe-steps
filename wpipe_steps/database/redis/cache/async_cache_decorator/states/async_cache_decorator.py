"""
Redis cache decorator operations (asynchronous).
"""

from typing import Any, Callable, Dict
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.decorators import async_cache


@step(
    name="redis_async_cache_decorator",
    version="v1.0",
    description="Async cache decorator for Redis",
    tags=["redis", "cache", "decorator", "async"]
)
class RedisAsyncCacheDecorator(BaseStep):
    """Apply async_cache decorator to a function (asynchronous)."""

    def __init__(
        self,
        ttl: int = 60,
        prefix: str = "default",
        name: str = None,
        version: str = "v1.0"
    ):
        super().__init__()
        self.ttl = ttl
        self.prefix = prefix
        self.name = name or "redis_async_cache_decorator"
        self.version = version

    @to_obj
    async def __call__(self, data: Any) -> Dict[str, Any]:
        """Return the async_cache decorator for use on functions.

        Args:
            data: Context data (unused).

        Returns:
            Dictionary with decorator.
        """
        try:
            decorator = async_cache(ttl=self.ttl, prefix=self.prefix)
            return {
                "success": True,
                "operation": "async_cache_decorator",
                "decorator": decorator,
                "ttl": self.ttl,
                "prefix": self.prefix
            }
        except Exception as e:
            return {
                "success": False,
                "operation": "async_cache_decorator",
                "error": str(e)
            }
