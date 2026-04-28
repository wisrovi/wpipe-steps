"""
Example: Redis Pipeline operations (asynchronous) using wpipe-steps.
"""

import asyncio
from wpipe_steps.database.redis.pipeline.execute_pipeline_async import RedisPipelineExecuteAsync


async def main():
    # Execute pipeline
    pipeline_step = RedisPipelineExecuteAsync(host="192.168.1.84")
    commands = [
        ("set", ["key1", "value1"]),
        ("set", ["key2", "value2"]),
        ("get", ["key1"])
    ]
    result = await pipeline_step({"commands": commands})
    print(f"Pipeline result: {result}")


if __name__ == "__main__":
    asyncio.run(main())
