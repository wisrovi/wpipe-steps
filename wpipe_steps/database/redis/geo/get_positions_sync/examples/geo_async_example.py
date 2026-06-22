"""
Example: Redis Geo operations (asynchronous) using wpipe-steps.
"""

import asyncio
from wpipe_steps.database.redis.geo.add_location_async import RedisGeoAddAsync
from wpipe_steps.database.redis.geo.get_distance_async import RedisGeoGetDistanceAsync


async def main():
    # Add location
    add_step = RedisGeoAddAsync(host="192.168.1.84")
    result = await add_step({"key": "cities", "member": "new_york", "longitude": -74.006, "latitude": 40.7128})
    print(f"Add location: {result}")

    # Get distance
    distance_step = RedisGeoGetDistanceAsync(host="192.168.1.84")
    result = await distance_step({"key": "cities", "member1": "new_york", "member2": "los_angeles", "unit": "km"})
    print(f"Distance: {result}")


if __name__ == "__main__":
    asyncio.run(main())
