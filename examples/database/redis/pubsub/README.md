# Redis Pub/Sub Examples

Examples of using Redis Pub/Sub operations with wpipe-steps.

## Files

- `pubsub_sync_example.py`: Synchronous pub/sub operations
- `pubsub_async_example.py`: Asynchronous pub/sub operations

## Usage

### Synchronous
```bash
python pubsub_sync_example.py
```

### Asynchronous
```bash
python pubsub_async_example.py
```

## Available Steps

### Synchronous
- `redis_pubsub_publish_sync`: Publish message to channel
- `redis_pubsub_on_message_sync`: Subscribe to channel (returns decorator)

### Asynchronous
- `redis_pubsub_publish_async`: Publish message to channel (async)
- `redis_pubsub_on_message_async`: Subscribe to channel (async, returns decorator)

## Prerequisites

- Redis server running at 192.168.1.84:6379
- Install dependencies: `pip install -r requirements.txt`
