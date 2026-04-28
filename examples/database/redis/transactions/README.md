# Redis Transactions Examples

Examples of using Redis transactions operations with wpipe-steps.

## Files

- `transactions_sync_example.py`: Synchronous transaction operations
- `transactions_async_example.py`: Asynchronous transaction operations

## Usage

### Synchronous
```bash
python transactions_sync_example.py
```

### Asynchronous
```bash
python transactions_async_example.py
```

## Available Steps

### Synchronous
- `redis_transaction_execute_sync`: Execute transaction with multiple commands

### Asynchronous
- `redis_transaction_execute_async`: Execute transaction with multiple commands (async)

## Prerequisites

- Redis server running at 192.168.1.84:6379
- Install dependencies: `pip install -r requirements.txt`
