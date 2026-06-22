"""
Example: Redis HyperLogLog operations (synchronous) using wpipe-steps.
"""

from wpipe_steps.database.redis.hyperloglog.add_sync import RedisHLLAddSync
from wpipe_steps.database.redis.hyperloglog.count_sync import RedisHLLCountSync

# Add to HyperLogLog
add_step = RedisHLLAddSync(host="192.168.1.84")
result = add_step({"key": "visitors", "values": ["user1", "user2", "user3"]})
print(f"Add to HLL: {result}")

# Count unique elements
count_step = RedisHLLCountSync(host="192.168.1.84")
result = count_step({"key": "visitors"})
print(f"Count HLL: {result}")
