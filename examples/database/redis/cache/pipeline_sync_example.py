"""
Example: Redis Cache decorators using wpipe Pipeline (synchronous).
"""

from wpipe import Pipeline
from wpipe_steps.database.redis.cache.cache_decorator_sync import RedisCacheDecoratorSync
from wpipe_steps.database.redis.cache.retry_decorator_sync import RedisRetryDecoratorSync


def main():
    """Run cache operations through wpipe Pipeline."""
    # Create pipeline
    pipeline = Pipeline(pipeline_name="cache_operations_sync")
    
    # Add steps to pipeline
    pipeline.set_steps([
        RedisCacheDecoratorSync.as_step(
            name="get_cache_decorator",
            ttl=60,
            prefix="myapp"
        ),
        RedisRetryDecoratorSync.as_step(
            name="get_retry_decorator",
            max_attempts=3,
            delay=0.1,
            backoff=1.0
        )
    ])
    
    # Run pipeline
    result = pipeline.run({})
    
    print(f"Pipeline result: {result}")
    return result


if __name__ == "__main__":
    main()
