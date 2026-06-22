"""
Example: Redis Sets operations (synchronous) using wpipe-steps.
"""

from wpipe_steps.database.redis.sets.add_to_set_sync import RedisSetAddSync
from wpipe_steps.database.redis.sets.get_set_members_sync import RedisSetGetMembersSync

# Add to set
add_step = RedisSetAddSync(host="192.168.1.84")
result = add_step({"key": "my_set", "values": ["value1", "value2"]})
print(f"Add to set: {result}")

# Get members
get_step = RedisSetGetMembersSync(host="192.168.1.84")
result = get_step({"key": "my_set"})
print(f"Get members: {result}")
