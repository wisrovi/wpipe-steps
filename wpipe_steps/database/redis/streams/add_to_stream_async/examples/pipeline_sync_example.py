"""
Example: Redis Streams operations using wpipe Pipeline (synchronous).
"""

from wpipe import Pipeline
from wpipe_steps.database.redis.streams.add_to_stream_sync import RedisStreamAddSync
from wpipe_steps.database.redis.streams.read_from_stream_sync import RedisStreamReadSync


def main():
    """Run streams operations through wpipe Pipeline."""
    # Create pipeline
    pipeline = Pipeline(pipeline_name="streams_operations_sync")
    
    # Add steps to pipeline
    pipeline.set_steps([
        RedisStreamAddSync.as_step(
            name="add_msg_1",
            host="192.168.1.84",
            key="my_stream",
            data={"field1": "value1"}
        ),
        RedisStreamAddSync.as_step(
            name="add_msg_2",
            host="192.168.1.84",
            key="my_stream",
            data={"field2": "value2"},
            ttl=300
        ),
        RedisStreamReadSync.as_step(
            name="read_stream",
            host="192.168.1.84",
            key="my_stream",
            count=10
        )
    ])
    
    # Run pipeline
    result = pipeline.run({})
    
    print(f"Pipeline result: {result}")
    return result


if __name__ == "__main__":
    main()
