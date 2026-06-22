"""
Example: Redis Hash operations using wpipe Pipeline (asynchronous).
"""

import asyncio
from wpipe import Pipeline
from wpipe_steps.database.redis.hash.create_hash_async import RedisHashCreateAsync
from wpipe_steps.database.redis.hash.read_hash_async import RedisHashReadAsync
from wpipe_steps.database.redis.hash.read_all_hash_async import RedisHashReadAllAsync


async def main():
    """Run hash operations through wpipe Pipeline asynchronously."""
    # Create pipeline
    pipeline = Pipeline(pipeline_name="hash_operations_async")
    
    # Add steps to pipeline
    pipeline.set_steps([
        RedisHashCreateAsync.as_step(
            name="create_hash_user1",
            host="192.168.1.84",
            hash_name="users",
            key="user:1",
            value={"name": "Alice", "age": 30},
            ttl=60
        ),
        RedisHashCreateAsync.as_step(
            name="create_hash_user2",
            host="192.168.1.84",
            hash_name="users",
            key="user:2",
            value={"name": "Bob", "age": 25}
        ),
        RedisHashReadAsync.as_step(
            name="read_hash_user1",
            host="192.168.1.84",
            hash_name="users",
            key="user:1"
        ),
        RedisHashReadAllAsync.as_step(
            name="read_all_users",
            host="192.168.1.84",
            hash_name="users"
        )
    ])
    
    # Run pipeline
    result = await pipeline.run({})
    
    print(f"Pipeline result: {result}")
    return result


if __name__ == "__main__":
    asyncio.run(main())
