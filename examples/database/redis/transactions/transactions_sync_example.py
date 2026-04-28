"""
Example: Redis Transactions operations (synchronous) using wpipe-steps.
"""

from wpipe_steps.database.redis.transactions.execute_transaction_sync import RedisTransactionExecuteSync

# Execute transaction
transaction_step = RedisTransactionExecuteSync(host="192.168.1.84")
commands = [
    ("set", ["balance:alice", "100"]),
    ("set", ["balance:bob", "50"]),
    ("incrby", ["balance:alice", 50]),
    ("get", ["balance:alice"])
]
result = transaction_step({"commands": commands})
print(f"Transaction result: {result}")
