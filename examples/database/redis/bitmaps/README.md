# Redis Bitmap Examples

Examples of using Redis bitmap operations with wpipe-steps.

## Files

- `bitmap_sync_example.py`: Synchronous bitmap operations
- `bitmap_async_example.py`: Asynchronous bitmap operations

## Usage

### Synchronous
```bash
python bitmap_sync_example.py
```

### Asynchronous
```bash
python bitmap_async_example.py
```

## Available Steps

### Synchronous
- `redis_bitmap_set_bit_sync`: Set a bit at offset
- `redis_bitmap_get_bit_sync`: Get bit at offset
- `redis_bitmap_count_bits_sync`: Count set bits
- `redis_bitmap_get_ttl_sync`: Get TTL of bitmap key
- `redis_bitmap_extend_ttl_sync`: Extend TTL of bitmap key

### Asynchronous
- `redis_bitmap_set_bit_async`: Set a bit at offset (async)
- `redis_bitmap_get_bit_async`: Get bit at offset (async)
- `redis_bitmap_count_bits_async`: Count set bits (async)
- `redis_bitmap_get_ttl_async`: Get TTL of bitmap key (async)
- `redis_bitmap_extend_ttl_async`: Extend TTL of bitmap key (async)

## Prerequisites

- Redis server running at 192.168.1.84:6379
- Install dependencies: `pip install -r requirements.txt`
