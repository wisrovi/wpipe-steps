"""
Example: Redis Hash operations (asynchronous) using wpipe-steps.
"""

import asyncio
from wpipe_steps.database.redis.hash.create_hash_async import RedisHashCreateAsync
from wpipe_steps.database.redis.hash.read_hash_async import RedisHashReadAsync
from wpipe_steps.database.redis.hash.update_hash_async import RedisHashUpdateAsync


async def main():
    # Create hash
    create_step = RedisHashCreateAsync(host="192.168.1.84")
    result = await create_step({"hash_name": "users", "key": "user:1", "value": {"name": "Alice", "age": 30}, "ttl": 60})
    print(f"Create hash: {result}")

    # Read hash
    read_step = RedisHashReadAsync(host="192.168.1.84")
    result = await read_step({"hash_name": "users", "key": "user:1"})
    print(f"Read hash: {result}")

    # Update hash
    update_step = RedisHashUpdateAsync(host="192.168.1.84")
    result = await update_step({"hash_name": "users", "key": "user:1", "new_data": {"name": "Alice", "age": 31}})
    print(f"Update hash: {result}")


if __name__ == "__main__":
    asyncio.run(main())
