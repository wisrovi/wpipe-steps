# Redis Streams Examples

Examples of using Redis streams operations with wpipe-steps.

## Files

- `streams_sync_example.py`: Synchronous streams operations
- `streams_async_example.py`: Asynchronous streams operations

## Usage

### Synchronous
```bash
python streams_sync_example.py
```

### Asynchronous
```bash
python streams_async_example.py
```

## Available Steps

### Synchronous
- `redis_stream_add_sync`: Add message to stream
- `redis_stream_read_sync`: Read messages from stream
- `redis_stream_on_message_sync`: Consume messages (returns decorator)

### Asynchronous
- `redis_stream_add_async`: Add message to stream (async)
- `redis_stream_read_async`: Read messages from stream (async)
- `redis_stream_on_message_async`: Consume messages (async, returns decorator)

## Prerequisites

- Redis server running at 192.168.1.84:6379
- Install dependencies: `pip install -r requirements.txt`
