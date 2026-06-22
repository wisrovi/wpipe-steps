"""
Example: Redis Sorted Sets operations (synchronous) using wpipe-steps.
"""

from wpipe_steps.database.redis.sortsets.add_to_sorted_set_sync import RedisSortsetsAddSync
from wpipe_steps.database.redis.sortsets.get_sorted_set_sync import RedisSortsetsGetSync

# Add to sorted set
add_step = RedisSortsetsAddSync(host="192.168.1.84")
result = add_step({"key": "my_sorted_set", "score": 1.0, "member": "item1"})
print(f"Add to sorted set: {result}")

# Get from sorted set
get_step = RedisSortsetsGetSync(host="192.168.1.84")
result = get_step({"key": "my_sorted_set", "with_scores": True})
print(f"Get sorted set: {result}")
