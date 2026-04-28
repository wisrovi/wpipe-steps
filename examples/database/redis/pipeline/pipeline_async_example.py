"""
Example: Redis Pipeline operations using wpipe Pipeline (asynchronous).
"""

import asyncio
from wpipe import Pipeline
from wpipe_steps.database.redis.pipeline.execute_pipeline_async import RedisPipelineExecuteAsync


async def main():
    """Run pipeline operations through wpipe Pipeline asynchronously."""
    # Create pipeline
    pipeline = Pipeline(pipeline_name="pipeline_operations_async")
    
    # Add steps to pipeline
    commands = [
        ("set", ["key1", "value1"]),
        ("set", ["key2", "value2"]),
        ("get", ["key1"])
    ]
    
    pipeline.set_steps([
        RedisPipelineExecuteAsync.as_step(
            name="execute_pipeline",
            host="192.168.1.84",
            commands=commands
        )
    ])
    
    # Run pipeline
    result = await pipeline.run({})
    
    print(f"Pipeline result: {result}")
    return result


if __name__ == "__main__":
    asyncio.run(main())
