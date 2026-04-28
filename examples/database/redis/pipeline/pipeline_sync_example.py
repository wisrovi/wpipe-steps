"""
Example: Redis Pipeline operations (synchronous) using wpipe-steps.
"""

from wpipe_steps.database.redis.pipeline.execute_pipeline_sync import RedisPipelineExecuteSync

# Execute pipeline
pipeline_step = RedisPipelineExecuteSync(host="192.168.1.84")
commands = [
    ("set", ["key1", "value1"]),
    ("set", ["key2", "value2"]),
    ("get", ["key1"])
]
result = pipeline_step({"commands": commands})
print(f"Pipeline result: {result}")
