"""
Example: Redis Geo operations using wpipe Pipeline (asynchronous).
"""

import asyncio
from wpipe import Pipeline
from wpipe_steps.database.redis.geo.add_location_async import RedisGeoAddAsync
from wpipe_steps.database.redis.geo.get_distance_async import RedisGeoGetDistanceAsync
from wpipe_steps.database.redis.geo.search_nearby_async import RedisGeoSearchNearbyAsync


async def main():
    """Run geo operations through wpipe Pipeline asynchronously."""
    # Create pipeline
    pipeline = Pipeline(pipeline_name="geo_operations_async")
    
    # Add steps to pipeline
    pipeline.set_steps([
        RedisGeoAddAsync.as_step(
            name="add_ny",
            host="192.168.1.84",
            key="cities",
            member="new_york",
            longitude=-74.006,
            latitude=40.7128
        ),
        RedisGeoAddAsync.as_step(
            name="add_la",
            host="192.168.1.84",
            key="cities",
            member="los_angeles",
            longitude=-118.2437,
            latitude=34.0522
        ),
        RedisGeoGetDistanceAsync.as_step(
            name="get_distance",
            host="192.168.1.84",
            key="cities",
            member1="new_york",
            member2="los_angeles",
            unit="km"
        ),
        RedisGeoSearchNearbyAsync.as_step(
            name="search_nearby",
            host="192.168.1.84",
            key="cities",
            longitude=-74.006,
            latitude=40.7128,
            radius=100,
            unit="km"
        )
    ])
    
    # Run pipeline
    result = await pipeline.run({})
    
    print(f"Pipeline result: {result}")
    return result


if __name__ == "__main__":
    asyncio.run(main())
