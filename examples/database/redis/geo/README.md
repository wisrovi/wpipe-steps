# Redis Geo Examples

Examples of using Redis geo operations with wpipe-steps.

## Files

- `geo_sync_example.py`: Synchronous geo operations
- `geo_async_example.py`: Asynchronous geo operations

## Usage

### Synchronous
```bash
python geo_sync_example.py
```

### Asynchronous
```bash
python geo_async_example.py
```

## Available Steps

### Synchronous
- `redis_geo_add_sync`: Add location to geo set
- `redis_geo_get_distance_sync`: Get distance between members
- `redis_geo_get_positions_sync`: Get positions of members
- `redis_geo_search_nearby_sync`: Search nearby members
- `redis_geo_search_nearby_dist_sync`: Search nearby with distance

### Asynchronous
- `redis_geo_add_async`: Add location to geo set (async)
- `redis_geo_get_distance_async`: Get distance between members (async)
- `redis_geo_get_positions_async`: Get positions of members (async)
- `redis_geo_search_nearby_async`: Search nearby members (async)
- `redis_geo_search_nearby_dist_async`: Search nearby with distance (async)

## Prerequisites

- Redis server running at 192.168.1.84:6379
- Install dependencies: `pip install -r requirements.txt`
