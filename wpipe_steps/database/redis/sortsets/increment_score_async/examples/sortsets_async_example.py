"""
Example: Redis Sorted Sets operations (asynchronous) using wpipe-steps.
"""

import asyncio
from wpipe_steps.database.redis.sortsets.add_to_sorted_set_async import RedisSortsetsAddAsync
from wpipe_steps.database.redis.sortsets.get_sorted_set_async import RedisSortsetsGetAsync


async def main():
    # Add to sorted set
    add_step = RedisSortsetsAddAsync(host="192.168.1.84")
    result = await add_step({"key": "my_sorted_set", "score": 1.0, "member": "item1"})
    print(f"Add to sorted set: {result}")

    # Get from sorted set
    get_step = RedisSortsetsGetAsync(host="192.168.1.84")
    result = await get_step({"key": "my_sorted_set", "with_scores": True})
    print(f"Get sorted set: {result}")


if __name__ == "__main__":
    asyncio.run(main())
