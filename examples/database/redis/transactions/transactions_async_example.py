"""
Example: Redis Transactions operations (asynchronous) using wpipe-steps.
"""

import asyncio
from wpipe_steps.database.redis.transactions.execute_transaction_async import RedisTransactionExecuteAsync


async def main():
    # Execute transaction
    transaction_step = RedisTransactionExecuteAsync(host="192.168.1.84")
    commands = [
        ("set", ["balance:alice", "100"]),
        ("set", ["balance:bob", "50"]),
        ("incrby", ["balance:alice", 50]),
        ("get", ["balance:alice"])
    ]
    result = await transaction_step({"commands": commands})
    print(f"Transaction result: {result}")


if __name__ == "__main__":
    asyncio.run(main())
