"""
Example: Redis Pub/Sub operations using wpipe Pipeline (synchronous).
"""

from wpipe import Pipeline
from wpipe_steps.database.redis.pubsub.publish_message_sync import RedisPubsubPublishSync


def main():
    """Run pubsub operations through wpipe Pipeline."""
    # Create pipeline
    pipeline = Pipeline(pipeline_name="pubsub_operations_sync")
    
    # Add steps to pipeline
    pipeline.set_steps([
        RedisPubsubPublishSync.as_step(
            name="publish_msg_1",
            host="192.168.1.84",
            channel="test_channel",
            message="Hello from wpipe!"
        ),
        RedisPubsubPublishSync.as_step(
            name="publish_msg_2",
            host="192.168.1.84",
            channel="test_channel",
            message={"type": "alert", "msg": "System check"}
        )
    ])
    
    # Run pipeline
    result = pipeline.run({})
    
    print(f"Pipeline result: {result}")
    return result


if __name__ == "__main__":
    main()
