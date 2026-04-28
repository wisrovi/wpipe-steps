# Redis HyperLogLog Examples

Examples of using Redis HyperLogLog operations with wpipe-steps.

## Files

- `hyperloglog_sync_example.py`: Synchronous HyperLogLog operations
- `hyperloglog_async_example.py`: Asynchronous HyperLogLog operations

## Usage

### Synchronous
```bash
python hyperloglog_sync_example.py
```

### Asynchronous
```bash
python hyperloglog_async_example.py
```

## Available Steps

### Synchronous
- `redis_hll_add_sync`: Add elements to HyperLogLog
- `redis_hll_count_sync`: Count unique elements

### Asynchronous
- `redis_hll_add_async`: Add elements to HyperLogLog (async)
- `redis_hll_count_async`: Count unique elements (async)

## Prerequisites

- Redis server running at 192.168.1.84:6379
- Install dependencies: `pip install -r requirements.txt`
