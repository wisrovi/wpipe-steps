"""
Redis retry decorator operations (synchronous).
"""

from typing import Any, Dict
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis._retry import retry


@step(
    name="redis_retry_decorator_sync",
    version="v1.0",
    description="Retry decorator for Redis operations (synchronous)",
    tags=["redis", "retry", "decorator", "sync"]
)
class RedisRetryDecoratorSync(BaseStep):
    """Apply retry decorator to a function (synchronous)."""

    def __init__(
        self,
        max_attempts: int = 3,
        delay: float = 0.1,
        backoff: float = 1.0,
        name: str = None,
        version: str = "v1.0"
    ):
        super().__init__()
        self.max_attempts = max_attempts
        self.delay = delay
        self.backoff = backoff
        self.name = name or "redis_retry_decorator_sync"
        self.version = version

    @to_obj
    def __call__(self, data: Any) -> Dict[str, Any]:
        """Return the retry decorator for use on functions.

        Args:
            data: Context data (unused).

        Returns:
            Dictionary with decorator.
        """
        try:
            decorator = retry(
                max_attempts=self.max_attempts,
                delay=self.delay,
                backoff=self.backoff
            )
            return {
                "success": True,
                "operation": "retry_decorator",
                "decorator": decorator,
                "max_attempts": self.max_attempts,
                "delay": self.delay,
                "backoff": self.backoff
            }
        except Exception as e:
            return {
                "success": False,
                "operation": "retry_decorator",
                "error": str(e)
            }
