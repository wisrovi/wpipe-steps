"""
Example: Redis HyperLogLog operations using wpipe Pipeline (asynchronous).
"""

import asyncio
from wpipe import Pipeline
from wpipe_steps.database.redis.hyperloglog.add_async import RedisHLLAddAsync
from wpipe_steps.database.redis.hyperloglog.count_async import RedisHLLCountAsync


async def main():
    """Run hyperloglog operations through wpipe Pipeline asynchronously."""
    # Create pipeline
    pipeline = Pipeline(pipeline_name="hyperloglog_operations_async")
    
    # Add steps to pipeline
    pipeline.set_steps([
        RedisHLLAddAsync.as_step(
            name="add_visitors_1",
            host="192.168.1.84",
            key="visitors",
            values=["user1", "user2", "user3"]
        ),
        RedisHLLAddAsync.as_step(
            name="add_visitors_2",
            host="192.168.1.84",
            key="visitors",
            values=["user4", "user5"]
        ),
        RedisHLLCountAsync.as_step(
            name="count_visitors",
            host="192.168.1.84",
            key="visitors"
        )
    ])
    
    # Run pipeline
    result = await pipeline.run({})
    
    print(f"Pipeline result: {result}")
    return result


if __name__ == "__main__":
    asyncio.run(main())
