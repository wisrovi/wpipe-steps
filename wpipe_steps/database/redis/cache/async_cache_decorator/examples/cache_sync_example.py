"""
Example: Redis Cache decorators (synchronous) using wpipe-steps.
"""

from wpipe_steps.database.redis.cache.cache_decorator_sync import RedisCacheDecoratorSync
from wpipe_steps.database.redis.cache.retry_decorator_sync import RedisRetryDecoratorSync

# Cache decorator example
cache_step = RedisCacheDecoratorSync(ttl=60, prefix="myapp")
result = cache_step({})
print(f"Cache decorator: {result}")

# Retry decorator example
retry_step = RedisRetryDecoratorSync(max_attempts=3, delay=0.1)
result = retry_step({})
print(f"Retry decorator: {result}")
