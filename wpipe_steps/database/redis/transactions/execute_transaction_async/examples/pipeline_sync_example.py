"""
Example: Redis Transactions operations using wpipe Pipeline (synchronous).
"""

from wpipe import Pipeline
from wpipe_steps.database.redis.transactions.execute_transaction_sync import RedisTransactionExecuteSync


def main():
    """Run transaction operations through wpipe Pipeline."""
    # Create pipeline
    pipeline = Pipeline(pipeline_name="transaction_operations_sync")
    
    # Add steps to pipeline
    commands = [
        ("set", ["balance:alice", "100"]),
        ("set", ["balance:bob", "50"]),
        ("incrby", ["balance:alice", 50]),
        ("get", ["balance:alice"])
    ]
    
    pipeline.set_steps([
        RedisTransactionExecuteSync.as_step(
            name="execute_transaction",
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
