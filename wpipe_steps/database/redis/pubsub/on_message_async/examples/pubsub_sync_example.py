"""
Example: Redis Pub/Sub operations (synchronous) using wpipe-steps.
"""

from wpipe_steps.database.redis.pubsub.publish_message_sync import RedisPubsubPublishSync

# Publish message
publish_step = RedisPubsubPublishSync(host="192.168.1.84")
result = publish_step({"channel": "test_channel", "message": "Hello Redis!"})
print(f"Publish result: {result}")
