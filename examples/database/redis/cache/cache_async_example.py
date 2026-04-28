"""
Example: Redis Cache decorators (asynchronous) using wpipe-steps.
"""

import asyncio
from wpipe_steps.database.redis.cache.async_cache_decorator import RedisAsyncCacheDecorator


async def main():
    # Async cache decorator example
    cache_step = RedisAsyncCacheDecorator(ttl=60, prefix="myapp")
    result = await cache_step({})
    print(f"Async cache decorator: {result}")


if __name__ == "__main__":
    asyncio.run(main())
