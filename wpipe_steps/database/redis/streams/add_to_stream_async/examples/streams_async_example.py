"""
Example: Redis Streams operations (asynchronous) using wpipe-steps.
"""

import asyncio
from wpipe_steps.database.redis.streams.add_to_stream_async import RedisStreamAddAsync
from wpipe_steps.database.redis.streams.read_from_stream_async import RedisStreamReadAsync


async def main():
    # Add to stream
    add_step = RedisStreamAddAsync(host="192.168.1.84")
    result = await add_step({"key": "my_stream", "data": {"field1": "value1"}, "ttl": 300})
    print(f"Add to stream: {result}")

    # Read from stream
    read_step = RedisStreamReadAsync(host="192.168.1.84")
    result = await read_step({"key": "my_stream", "count": 10})
    print(f"Read from stream: {result}")


if __name__ == "__main__":
    asyncio.run(main())
