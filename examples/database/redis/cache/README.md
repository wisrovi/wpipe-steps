# Redis Cache Examples

Examples of using Redis cache decorators with wpipe-steps.

## Files

- `cache_sync_example.py`: Synchronous cache/retry decorators
- `cache_async_example.py`: Asynchronous cache decorator

## Usage

### Synchronous
```bash
python cache_sync_example.py
```

### Asynchronous
```bash
python cache_async_example.py
```

## Available Steps

### Synchronous
- `redis_cache_decorator_sync`: Get cache decorator with TTL
- `redis_retry_decorator_sync`: Get retry decorator with backoff

### Asynchronous
- `redis_async_cache_decorator`: Get async cache decorator with TTL

## Prerequisites

- Redis server running at 192.168.1.84:6379
- Install dependencies: `pip install -r requirements.txt`
