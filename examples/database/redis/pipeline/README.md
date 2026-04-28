# Redis Pipeline Examples

Examples of using Redis pipeline operations with wpipe-steps.

## Files

- `pipeline_sync_example.py`: Synchronous pipeline operations
- `pipeline_async_example.py`: Asynchronous pipeline operations

## Usage

### Synchronous
```bash
python pipeline_sync_example.py
```

### Asynchronous
```bash
python pipeline_async_example.py
```

## Available Steps

### Synchronous
- `redis_pipeline_execute_sync`: Execute pipeline with multiple commands

### Asynchronous
- `redis_pipeline_execute_async`: Execute pipeline with multiple commands (async)

## Prerequisites

- Redis server running at 192.168.1.84:6379
- Install dependencies: `pip install -r requirements.txt`
