"""
Redis cache decorator operations (synchronous).
"""

from typing import Any, Callable, Dict
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.decorators import cache


@step(
    name="redis_cache_decorator_sync",
    version="v1.0",
    description="Cache decorator for Redis (synchronous)",
    tags=["redis", "cache", "decorator", "sync"]
)
class RedisCacheDecoratorSync(BaseStep):
    """Apply cache decorator to a function (synchronous)."""

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
        self.name = name or "redis_cache_decorator_sync"
        self.version = version

    @to_obj
    def __call__(self, data: Any) -> Dict[str, Any]:
        """Return the cache decorator for use on functions.

        Args:
            data: Context data (unused).

        Returns:
            Dictionary with decorator.
        """
        try:
            decorator = cache(ttl=self.ttl, prefix=self.prefix)
            return {
                "success": True,
                "operation": "cache_decorator",
                "decorator": decorator,
                "ttl": self.ttl,
                "prefix": self.prefix
            }
        except Exception as e:
            return {
                "success": False,
                "operation": "cache_decorator",
                "error": str(e)
            }
