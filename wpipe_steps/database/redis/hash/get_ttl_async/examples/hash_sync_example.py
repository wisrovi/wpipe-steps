"""
Example: Redis Hash operations (synchronous) using wpipe-steps.
"""

from wpipe_steps.database.redis.hash.create_hash_sync import RedisHashCreateSync
from wpipe_steps.database.redis.hash.read_hash_sync import RedisHashReadSync
from wpipe_steps.database.redis.hash.update_hash_sync import RedisHashUpdateSync

# Create hash
create_step = RedisHashCreateSync(host="192.168.1.84")
result = create_step({"hash_name": "users", "key": "user:1", "value": {"name": "Alice", "age": 30}, "ttl": 60})
print(f"Create hash: {result}")

# Read hash
read_step = RedisHashReadSync(host="192.168.1.84")
result = read_step({"hash_name": "users", "key": "user:1"})
print(f"Read hash: {result}")

# Update hash
update_step = RedisHashUpdateSync(host="192.168.1.84")
result = update_step({"hash_name": "users", "key": "user:1", "new_data": {"name": "Alice", "age": 31}})
print(f"Update hash: {result}")
