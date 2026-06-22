"""
Example: Redis Queue operations using wpipe Pipeline (asynchronous).
"""

import asyncio
from wpipe import Pipeline
from wpipe_steps.database.redis.queue.publish_async import RedisQueuePublishAsync
from wpipe_steps.database.redis.queue.get_queue_length_async import RedisQueueGetLengthAsync


async def main():
    """Run queue operations through wpipe Pipeline asynchronously."""
    # Create pipeline
    pipeline = Pipeline(pipeline_name="queue_operations_async")
    
    # Add steps to pipeline
    pipeline.set_steps([
        RedisQueuePublishAsync.as_step(
            name="publish_task_1",
            host="192.168.1.84",
            queue_name="tasks",
            data={"id": 1, "task": "process_image"},
            ttl=30
        ),
        RedisQueuePublishAsync.as_step(
            name="publish_task_2",
            host="192.168.1.84",
            queue_name="tasks",
            data={"id": 2, "task": "generate_report"}
        ),
        RedisQueueGetLengthAsync.as_step(
            name="get_queue_length",
            host="192.168.1.84",
            queue_name="tasks"
        )
    ])
    
    # Run pipeline
    result = await pipeline.run({})
    
    print(f"Pipeline result: {result}")
    return result


if __name__ == "__main__":
    asyncio.run(main())
