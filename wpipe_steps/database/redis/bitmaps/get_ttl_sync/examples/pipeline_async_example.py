"""
Example: Redis Bitmap operations using wpipe Pipeline (asynchronous).
"""

import asyncio
from wpipe import Pipeline
from wpipe_steps.database.redis.bitmaps.set_bit_async import RedisBitmapSetBitAsync
from wpipe_steps.database.redis.bitmaps.get_bit_async import RedisBitmapGetBitAsync
from wpipe_steps.database.redis.bitmaps.count_bits_async import RedisBitmapCountBitsAsync


async def main():
    """Run bitmap operations through wpipe Pipeline asynchronously."""
    # Create pipeline
    pipeline = Pipeline(pipeline_name="bitmap_operations_async")
    
    # Add steps to pipeline
    pipeline.set_steps([
        RedisBitmapSetBitAsync.as_step(
            name="set_bit_5",
            host="192.168.1.84",
            offset=5,
            value=1,
            ttl=300
        ),
        RedisBitmapGetBitAsync.as_step(
            name="get_bit_5",
            host="192.168.1.84",
            offset=5
        ),
        RedisBitmapCountBitsAsync.as_step(
            name="count_bits",
            host="192.168.1.84"
        )
    ])
    
    # Run pipeline
    result = await pipeline.run({"key": "my_bitmap"})
    
    print(f"Pipeline result: {result}")
    return result


if __name__ == "__main__":
    asyncio.run(main())
