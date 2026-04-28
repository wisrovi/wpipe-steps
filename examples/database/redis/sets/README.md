# Redis Sets Examples

Examples of using Redis sets operations with wpipe-steps.

## Files

- `sets_sync_example.py`: Synchronous sets operations
- `sets_async_example.py`: Asynchronous sets operations

## Usage

### Synchronous
```bash
python sets_sync_example.py
```

### Asynchronous
```bash
python sets_async_example.py
```

## Available Steps

### Synchronous
- `redis_set_add_sync`: Add members to set
- `redis_set_get_members_sync`: Get all members
- `redis_set_is_member_sync`: Check membership
- `redis_set_remove_sync`: Remove members
- `redis_set_get_ttl_sync`: Get TTL
- `redis_set_extend_ttl_sync`: Extend TTL

### Asynchronous
- `redis_set_add_async`: Add members to set (async)
- `redis_set_get_members_async`: Get all members (async)
- `redis_set_is_member_async`: Check membership (async)
- `redis_set_remove_async`: Remove members (async)
- `redis_set_get_ttl_async`: Get TTL (async)
- `redis_set_extend_ttl_async`: Extend TTL (async)

## Prerequisites

- Redis server running at 192.168.1.84:6379
- Install dependencies: `pip install -r requirements.txt`
