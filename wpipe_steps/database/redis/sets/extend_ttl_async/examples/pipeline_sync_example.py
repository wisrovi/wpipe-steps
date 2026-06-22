"""
Example: Redis Sets operations using wpipe Pipeline (synchronous).
"""

from wpipe import Pipeline
from wpipe_steps.database.redis.sets.add_to_set_sync import RedisSetAddSync
from wpipe_steps.database.redis.sets.get_set_members_sync import RedisSetGetMembersSync
from wpipe_steps.database.redis.sets.is_member_sync import RedisSetIsMemberSync


def main():
    """Run sets operations through wpipe Pipeline."""
    # Create pipeline
    pipeline = Pipeline(pipeline_name="sets_operations_sync")
    
    # Add steps to pipeline
    pipeline.set_steps([
        RedisSetAddSync.as_step(
            name="add_members",
            host="192.168.1.84",
            key="my_set",
            values=["value1", "value2", "value3"]
        ),
        RedisSetGetMembersSync.as_step(
            name="get_members",
            host="192.168.1.84",
            key="my_set"
        ),
        RedisSetIsMemberSync.as_step(
            name="check_member",
            host="192.168.1.84",
            key="my_set",
            value="value1"
        )
    ])
    
    # Run pipeline
    result = pipeline.run({})
    
    print(f"Pipeline result: {result}")
    return result


if __name__ == "__main__":
    main()
