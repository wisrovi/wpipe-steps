"""
Example: Redis HyperLogLog operations (asynchronous) using wpipe-steps.
"""

import asyncio
from wpipe_steps.database.redis.hyperloglog.add_async import RedisHLLAddAsync
from wpipe_steps.database.redis.hyperloglog.count_async import RedisHLLCountAsync


async def main():
    # Add to HyperLogLog
    add_step = RedisHLLAddAsync(host="192.168.1.84")
    result = await add_step({"key": "visitors", "values": ["user1", "user2", "user3"]})
    print(f"Add to HLL: {result}")

    # Count unique elements
    count_step = RedisHLLCountAsync(host="192.168.1.84")
    result = await count_step({"key": "visitors"})
    print(f"Count HLL: {result}")


if __name__ == "__main__":
    asyncio.run(main())
