"""
Example: Redis Sets operations (asynchronous) using wpipe-steps.
"""

import asyncio
from wpipe_steps.database.redis.sets.add_to_set_async import RedisSetAddAsync
from wpipe_steps.database.redis.sets.get_set_members_async import RedisSetGetMembersAsync


async def main():
    # Add to set
    add_step = RedisSetAddAsync(host="192.168.1.84")
    result = await add_step({"key": "my_set", "values": ["value1", "value2"]})
    print(f"Add to set: {result}")

    # Get members
    get_step = RedisSetGetMembersAsync(host="192.168.1.84")
    result = await get_step({"key": "my_set"})
    print(f"Get members: {result}")


if __name__ == "__main__":
    asyncio.run(main())
