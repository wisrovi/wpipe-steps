"""
Example: Redis Bitmap operations (asynchronous) using wpipe-steps.
"""

import asyncio
from wpipe_steps.database.redis.bitmaps.set_bit_async import RedisBitmapSetBitAsync
from wpipe_steps.database.redis.bitmaps.get_bit_async import RedisBitmapGetBitAsync
from wpipe_steps.database.redis.bitmaps.count_bits_async import RedisBitmapCountBitsAsync


async def main():
    # Set bit example
    set_bit_step = RedisBitmapSetBitAsync(host="192.168.1.84")
    result = await set_bit_step({"key": "my_bitmap", "offset": 5, "value": 1})
    print(f"Set bit result: {result}")

    # Get bit example
    get_bit_step = RedisBitmapGetBitAsync(host="192.168.1.84")
    result = await get_bit_step({"key": "my_bitmap", "offset": 5})
    print(f"Get bit result: {result}")

    # Count bits example
    count_step = RedisBitmapCountBitsAsync(host="192.168.1.84")
    result = await count_step({"key": "my_bitmap"})
    print(f"Count bits result: {result}")


if __name__ == "__main__":
    asyncio.run(main())
