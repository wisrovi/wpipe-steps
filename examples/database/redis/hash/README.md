# Redis Hash Examples

Examples of using Redis hash operations with wpipe-steps.

## Files

- `hash_sync_example.py`: Synchronous hash operations
- `hash_async_example.py`: Asynchronous hash operations

## Usage

### Synchronous
```bash
python hash_sync_example.py
```

### Asynchronous
```bash
python hash_async_example.py
```

## Available Steps

### Synchronous
- `redis_hash_create_sync`: Create hash field
- `redis_hash_read_sync`: Read hash field
- `redis_hash_read_all_sync`: Read all hash fields
- `redis_hash_update_sync`: Update hash field
- `redis_hash_delete_sync`: Delete hash field
- `redis_hash_get_ttl_sync`: Get TTL
- `redis_hash_extend_ttl_sync`: Extend TTL

### Asynchronous
- `redis_hash_create_async`: Create hash field (async)
- `redis_hash_read_async`: Read hash field (async)
- `redis_hash_read_all_async`: Read all hash fields (async)
- `redis_hash_update_async`: Update hash field (async)
- `redis_hash_delete_async`: Delete hash field (async)
- `redis_hash_get_ttl_async`: Get TTL (async)
- `redis_hash_extend_ttl_async`: Extend TTL (async)

## Prerequisites

- Redis server running at 192.168.1.84:6379
- Install dependencies: `pip install -r requirements.txt`
