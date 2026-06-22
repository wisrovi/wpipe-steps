"""
Example: Redis Queue operations using wpipe Pipeline (synchronous).
"""

from wpipe import Pipeline
from wpipe_steps.database.redis.queue.publish_sync import RedisQueuePublishSync
from wpipe_steps.database.redis.queue.get_queue_length_sync import RedisQueueGetLengthSync


def main():
    """Run queue operations through wpipe Pipeline."""
    # Create pipeline
    pipeline = Pipeline(pipeline_name="queue_operations_sync")
    
    # Add steps to pipeline
    pipeline.set_steps([
        RedisQueuePublishSync.as_step(
            name="publish_task_1",
            host="192.168.1.84",
            queue_name="tasks",
            data={"id": 1, "task": "process_image"},
            ttl=30
        ),
        RedisQueuePublishSync.as_step(
            name="publish_task_2",
            host="192.168.1.84",
            queue_name="tasks",
            data={"id": 2, "task": "generate_report"}
        ),
        RedisQueueGetLengthSync.as_step(
            name="get_queue_length",
            host="192.168.1.84",
            queue_name="tasks"
        )
    ])
    
    # Run pipeline
    result = pipeline.run({})
    
    print(f"Pipeline result: {result}")
    return result


if __name__ == "__main__":
    main()
