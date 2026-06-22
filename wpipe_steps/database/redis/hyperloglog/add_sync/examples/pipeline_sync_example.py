"""
Example: Redis HyperLogLog operations using wpipe Pipeline (synchronous).
"""

from wpipe import Pipeline
from wpipe_steps.database.redis.hyperloglog.add_sync import RedisHLLAddSync
from wpipe_steps.database.redis.hyperloglog.count_sync import RedisHLLCountSync


def main():
    """Run hyperloglog operations through wpipe Pipeline."""
    # Create pipeline
    pipeline = Pipeline(pipeline_name="hyperloglog_operations_sync")
    
    # Add steps to pipeline
    pipeline.set_steps([
        RedisHLLAddSync.as_step(
            name="add_visitors_1",
            host="192.168.1.84",
            key="visitors",
            values=["user1", "user2", "user3"]
        ),
        RedisHLLAddSync.as_step(
            name="add_visitors_2",
            host="192.168.1.84",
            key="visitors",
            values=["user4", "user5"]
        ),
        RedisHLLCountSync.as_step(
            name="count_visitors",
            host="192.168.1.84",
            key="visitors"
        )
    ])
    
    # Run pipeline
    result = pipeline.run({})
    
    print(f"Pipeline result: {result}")
    return result


if __name__ == "__main__":
    main()
