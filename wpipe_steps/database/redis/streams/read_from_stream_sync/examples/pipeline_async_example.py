"""
Example: Redis Streams operations using wpipe Pipeline (asynchronous).
"""

import asyncio
from wpipe import Pipeline
from wpipe_steps.database.redis.streams.add_to_stream_async import RedisStreamAddAsync
from wpipe_steps.database.redis.streams.read_from_stream_async import RedisStreamReadAsync


async def main():
    """Run streams operations through wpipe Pipeline asynchronously."""
    # Create pipeline
    pipeline = Pipeline(pipeline_name="streams_operations_async")
    
    # Add steps to pipeline
    pipeline.set_steps([
        RedisStreamAddAsync.as_step(
            name="add_msg_1",
            host="192.168.1.84",
            key="my_stream",
            data={"field1": "value1"}
        ),
        RedisStreamAddAsync.as_step(
            name="add_msg_2",
            host="192.168.1.84",
            key="my_stream",
            data={"field2": "value2"},
            ttl=300
        ),
        RedisStreamReadAsync.as_step(
            name="read_stream",
            host="192.168.1.84",
            key="my_stream",
            count=10
        )
    ])
    
    # Run pipeline
    result = await pipeline.run({})
    
    print(f"Pipeline result: {result}")
    return result


if __name__ == "__main__":
    asyncio.run(main())
