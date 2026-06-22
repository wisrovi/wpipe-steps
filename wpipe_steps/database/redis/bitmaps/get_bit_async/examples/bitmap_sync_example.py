"""
Example: Redis Bitmap operations (synchronous) using wpipe-steps.
"""

from wpipe_steps.database.redis.bitmaps.set_bit_sync import RedisBitmapSetBitSync
from wpipe_steps.database.redis.bitmaps.get_bit_sync import RedisBitmapGetBitSync
from wpipe_steps.database.redis.bitmaps.count_bits_sync import RedisBitmapCountBitsSync

# Set bit example
set_bit_step = RedisBitmapSetBitSync(host="192.168.1.84")
result = set_bit_step({"key": "my_bitmap", "offset": 5, "value": 1})
print(f"Set bit result: {result}")

# Get bit example
get_bit_step = RedisBitmapGetBitSync(host="192.168.1.84")
result = get_bit_step({"key": "my_bitmap", "offset": 5})
print(f"Get bit result: {result}")

# Count bits example
count_step = RedisBitmapCountBitsSync(host="192.168.1.84")
result = count_step({"key": "my_bitmap"})
print(f"Count bits result: {result}")
