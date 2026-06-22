"""
Example: Redis Bitmap operations using wpipe Pipeline (synchronous).
"""

from wpipe import Pipeline
from wpipe_steps.database.redis.bitmaps.set_bit_sync import RedisBitmapSetBitSync
from wpipe_steps.database.redis.bitmaps.get_bit_sync import RedisBitmapGetBitSync
from wpipe_steps.database.redis.bitmaps.count_bits_sync import RedisBitmapCountBitsSync


def main():
    """Run bitmap operations through wpipe Pipeline."""
    # Create pipeline
    pipeline = Pipeline(pipeline_name="bitmap_operations_sync")
    
    # Add steps to pipeline
    pipeline.set_steps([
        RedisBitmapSetBitSync.as_step(
            name="set_bit_5",
            host="192.168.1.84",
            offset=5,
            value=1,
            ttl=300
        ),
        RedisBitmapGetBitSync.as_step(
            name="get_bit_5",
            host="192.168.1.84",
            offset=5
        ),
        RedisBitmapCountBitsSync.as_step(
            name="count_bits",
            host="192.168.1.84"
        )
    ])
    
    # Run pipeline
    result = pipeline.run({"key": "my_bitmap"})
    
    print(f"Pipeline result: {result}")
    return result


if __name__ == "__main__":
    main()
