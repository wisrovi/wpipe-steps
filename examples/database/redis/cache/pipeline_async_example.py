"""
Example: Redis Cache decorators using wpipe Pipeline (asynchronous).
"""

import asyncio
from wpipe import Pipeline
from wpipe_steps.database.redis.cache.async_cache_decorator import RedisAsyncCacheDecorator


async def main():
    """Run cache operations through wpipe Pipeline asynchronously."""
    # Create pipeline
    pipeline = Pipeline(pipeline_name="cache_operations_async")
    
    # Add steps to pipeline
    pipeline.set_steps([
        RedisAsyncCacheDecorator.as_step(
            name="get_async_cache_decorator",
            ttl=60,
            prefix="myapp"
        )
    ])
    
    # Run pipeline
    result = await pipeline.run({})
    
    print(f"Pipeline result: {result}")
    return result


if __name__ == "__main__":
    asyncio.run(main())
