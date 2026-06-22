"""
Example: Redis Geo operations (synchronous) using wpipe-steps.
"""

from wpipe_steps.database.redis.geo.add_location_sync import RedisGeoAddSync
from wpipe_steps.database.redis.geo.get_distance_sync import RedisGeoGetDistanceSync

# Add location
add_step = RedisGeoAddSync(host="192.168.1.84")
result = add_step({"key": "cities", "member": "new_york", "longitude": -74.006, "latitude": 40.7128})
print(f"Add location: {result}")

# Get distance
distance_step = RedisGeoGetDistanceSync(host="192.168.1.84")
result = distance_step({"key": "cities", "member1": "new_york", "member2": "los_angeles", "unit": "km"})
print(f"Distance: {result}")
