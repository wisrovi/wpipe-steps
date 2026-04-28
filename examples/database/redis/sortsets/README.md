# Redis Sorted Sets Examples

Examples of using Redis sorted sets operations with wpipe-steps.

## Files

- `sortsets_sync_example.py`: Synchronous sorted sets operations
- `sortsets_async_example.py`: Asynchronous sorted sets operations

## Usage

### Synchronous
```bash
python sortsets_sync_example.py
```

### Asynchronous
```bash
python sortsets_async_example.py
```

## Available Steps

### Synchronous
- `redis_sortsets_add_sync`: Add member to sorted set
- `redis_sortsets_get_sync`: Get members (ascending)
- `redis_sortsets_get_reverse_sync`: Get members (descending)
- `redis_sortsets_remove_sync`: Remove member
- `redis_sortsets_get_rank_sync`: Get rank of member
- `redis_sortsets_get_score_sync`: Get score of member
- `redis_sortsets_increment_score_sync`: Increment score
- `redis_sortsets_get_by_score_sync`: Get by score range
- `redis_sortsets_delete_sync`: Delete sorted set
- `redis_sortsets_set_ttl_sync`: Set TTL
- `redis_sortsets_get_ttl_sync`: Get TTL

### Asynchronous
- `redis_sortsets_add_async`: Add member to sorted set (async)
- `redis_sortsets_get_async`: Get members (ascending, async)
- `redis_sortsets_get_reverse_async`: Get members (descending, async)
- `redis_sortsets_remove_async`: Remove member (async)
- `redis_sortsets_get_rank_async`: Get rank of member (async)
- `redis_sortsets_get_score_async`: Get score of member (async)
- `redis_sortsets_increment_score_async`: Increment score (async)
- `redis_sortsets_get_by_score_async`: Get by score range (async)
- `redis_sortsets_delete_async`: Delete sorted set (async)
- `redis_sortsets_set_ttl_async`: Set TTL (async)
- `redis_sortsets_get_ttl_async`: Get TTL (async)

## Prerequisites

- Redis server running at 192.168.1.84:6379
- Install dependencies: `pip install -r requirements.txt`
