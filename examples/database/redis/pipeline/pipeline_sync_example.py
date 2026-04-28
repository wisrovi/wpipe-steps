"""
Example: Redis Pipeline operations using wpipe Pipeline (synchronous).
"""

from wpipe import Pipeline
from wpipe_steps.database.redis.pipeline.execute_pipeline_sync import RedisPipelineExecuteSync


def main():
    """Run pipeline operations through wpipe Pipeline."""
    # Create pipeline
    pipeline = Pipeline(pipeline_name="pipeline_operations_sync")
    
    # Add steps to pipeline
    commands = [
        ("set", ["key1", "value1"]),
        ("set", ["key2", "value2"]),
        ("get", ["key1"])
    ]
    
    pipeline.set_steps([
        RedisPipelineExecuteSync.as_step(
            name="execute_pipeline",
            host="192.168.1.84",
            commands=commands
        )
    ])
    
    # Run pipeline
    result = pipeline.run({})
    
    print(f"Pipeline result: {result}")
    return result


if __name__ == "__main__":
    main()
