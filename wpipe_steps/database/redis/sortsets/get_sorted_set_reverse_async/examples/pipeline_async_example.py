"""
Example: Redis Sorted Sets operations using wpipe Pipeline (asynchronous).
"""

import asyncio
from wpipe import Pipeline
from wpipe_steps.database.redis.sortsets.add_to_sorted_set_async import RedisSortsetsAddAsync
from wpipe_steps.database.redis.sortsets.get_sorted_set_async import RedisSortsetsGetAsync
from wpipe_steps.database.redis.sortsets.get_rank_async import RedisSortsetsGetRankAsync


async def main():
    """Run sorted sets operations through wpipe Pipeline asynchronously."""
    # Create pipeline
    pipeline = Pipeline(pipeline_name="sortsets_operations_async")
    
    # Add steps to pipeline
    pipeline.set_steps([
        RedisSortsetsAddAsync.as_step(
            name="add_item1",
            host="192.168.1.84",
            key="my_sorted_set",
            score=1.0,
            member="item1"
        ),
        RedisSortsetsAddAsync.as_step(
            name="add_item2",
            host="192.168.1.84",
            key="my_sorted_set",
            score=3.0,
            member="item2"
        ),
        RedisSortsetsGetAsync.as_step(
            name="get_sorted",
            host="192.168.1.84",
            key="my_sorted_set",
            with_scores=True
        ),
        RedisSortsetsGetRankAsync.as_step(
            name="get_rank",
            host="192.168.1.84",
            key="my_sorted_set",
            member="item1"
        )
    ])
    
    # Run pipeline
    result = await pipeline.run({})
    
    print(f"Pipeline result: {result}")
    return result


if __name__ == "__main__":
    asyncio.run(main())
