"""
Example: Redis Pub/Sub operations (asynchronous) using wpipe-steps.
"""

import asyncio
from wpipe_steps.database.redis.pubsub.publish_message_async import RedisPubsubPublishAsync


async def main():
    # Publish message
    publish_step = RedisPubsubPublishAsync(host="192.168.1.84")
    result = await publish_step({"channel": "test_channel", "message": "Hello Redis!"})
    print(f"Publish result: {result}")


if __name__ == "__main__":
    asyncio.run(main())
