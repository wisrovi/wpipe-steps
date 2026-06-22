"""
Example: Redis Sorted Sets operations using wpipe Pipeline (synchronous).
"""

from wpipe import Pipeline
from wpipe_steps.database.redis.sortsets.add_to_sorted_set_sync import RedisSortsetsAddSync
from wpipe_steps.database.redis.sortsets.get_sorted_set_sync import RedisSortsetsGetSync
from wpipe_steps.database.redis.sortsets.get_rank_sync import RedisSortsetsGetRankSync


def main():
    """Run sorted sets operations through wpipe Pipeline."""
    # Create pipeline
    pipeline = Pipeline(pipeline_name="sortsets_operations_sync")
    
    # Add steps to pipeline
    pipeline.set_steps([
        RedisSortsetsAddSync.as_step(
            name="add_item1",
            host="192.168.1.84",
            key="my_sorted_set",
            score=1.0,
            member="item1"
        ),
        RedisSortsetsAddSync.as_step(
            name="add_item2",
            host="192.168.1.84",
            key="my_sorted_set",
            score=3.0,
            member="item2"
        ),
        RedisSortsetsGetSync.as_step(
            name="get_sorted",
            host="192.168.1.84",
            key="my_sorted_set",
            with_scores=True
        ),
        RedisSortsetsGetRankSync.as_step(
            name="get_rank",
            host="192.168.1.84",
            key="my_sorted_set",
            member="item1"
        )
    ])
    
    # Run pipeline
    result = pipeline.run({})
    
    print(f"Pipeline result: {result}")
    return result


if __name__ == "__main__":
    main()
