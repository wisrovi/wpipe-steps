"""
Example: Redis Sets operations using wpipe Pipeline (asynchronous).
"""

import asyncio
from wpipe import Pipeline
from wpipe_steps.database.redis.sets.add_to_set_async import RedisSetAddAsync
from wpipe_steps.database.redis.sets.get_set_members_async import RedisSetGetMembersAsync
from wpipe_steps.database.redis.sets.is_member_async import RedisSetIsMemberAsync


async def main():
    """Run sets operations through wpipe Pipeline asynchronously."""
    # Create pipeline
    pipeline = Pipeline(pipeline_name="sets_operations_async")
    
    # Add steps to pipeline
    pipeline.set_steps([
        RedisSetAddAsync.as_step(
            name="add_members",
            host="192.168.1.84",
            key="my_set",
            values=["value1", "value2", "value3"]
        ),
        RedisSetGetMembersAsync.as_step(
            name="get_members",
            host="192.168.1.84",
            key="my_set"
        ),
        RedisSetIsMemberAsync.as_step(
            name="check_member",
            host="192.168.1.84",
            key="my_set",
            value="value1"
        )
    ])
    
    # Run pipeline
    result = await pipeline.run({})
    
    print(f"Pipeline result: {result}")
    return result


if __name__ == "__main__":
    asyncio.run(main())
