"""
Example: Redis Hash operations using wpipe Pipeline (synchronous).
"""

from wpipe import Pipeline
from wpipe_steps.database.redis.hash.create_hash_sync import RedisHashCreateSync
from wpipe_steps.database.redis.hash.read_hash_sync import RedisHashReadSync
from wpipe_steps.database.redis.hash.read_all_hash_sync import RedisHashReadAllSync


def main():
    """Run hash operations through wpipe Pipeline."""
    # Create pipeline
    pipeline = Pipeline(pipeline_name="hash_operations_sync")
    
    # Add steps to pipeline
    pipeline.set_steps([
        RedisHashCreateSync.as_step(
            name="create_hash_user1",
            host="192.168.1.84",
            hash_name="users",
            key="user:1",
            value={"name": "Alice", "age": 30},
            ttl=60
        ),
        RedisHashCreateSync.as_step(
            name="create_hash_user2",
            host="192.168.1.84",
            hash_name="users",
            key="user:2",
            value={"name": "Bob", "age": 25}
        ),
        RedisHashReadSync.as_step(
            name="read_hash_user1",
            host="192.168.1.84",
            hash_name="users",
            key="user:1"
        ),
        RedisHashReadAllSync.as_step(
            name="read_all_users",
            host="192.168.1.84",
            hash_name="users"
        )
    ])
    
    # Run pipeline
    result = pipeline.run({})
    
    print(f"Pipeline result: {result}")
    return result


if __name__ == "__main__":
    main()
