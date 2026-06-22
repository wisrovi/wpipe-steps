"""
Example: Redis Streams operations (synchronous) using wpipe-steps.
"""

from wpipe_steps.database.redis.streams.add_to_stream_sync import RedisStreamAddSync
from wpipe_steps.database.redis.streams.read_from_stream_sync import RedisStreamReadSync

# Add to stream
add_step = RedisStreamAddSync(host="192.168.1.84")
result = add_step({"key": "my_stream", "data": {"field1": "value1"}, "ttl": 300})
print(f"Add to stream: {result}")

# Read from stream
read_step = RedisStreamReadSync(host="192.168.1.84")
result = read_step({"key": "my_stream", "count": 10})
print(f"Read from stream: {result}")
