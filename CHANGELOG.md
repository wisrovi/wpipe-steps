# WPipe Changelog

All notable changes to WPipe will be documented in this file.

---

## [0.25.0] - 2026-04-28

### Added
- **Redis Pub/Sub Module**: Complete pub/sub operations support
  - `redis_pubsub_publish_sync` / `redis_pubsub_publish_async`: Publish messages
  - `redis_pubsub_on_message_sync` / `redis_pubsub_on_message_async`: Subscribe to channels
- Examples for pubsub module in `examples/database/redis/pubsub/`

---

## [0.24.0] - 2026-04-28

### Added
- **Redis Hash Module**: Complete hash operations support
  - `redis_hash_create_sync` / `redis_hash_create_async`: Create hash field
  - `redis_hash_read_sync` / `redis_hash_read_async`: Read hash field
  - `redis_hash_read_all_sync` / `redis_hash_read_all_async`: Read all hash fields
  - `redis_hash_update_sync` / `redis_hash_update_async`: Update hash field
  - `redis_hash_delete_sync` / `redis_hash_delete_async`: Delete hash field
  - `redis_hash_get_ttl_sync` / `redis_hash_get_ttl_async`: Get TTL
  - `redis_hash_extend_ttl_sync` / `redis_hash_extend_ttl_async`: Extend TTL
- Examples for hash module in `examples/database/redis/hash/`

---

## [0.23.0] - 2026-04-28

### Added
- **Redis Bitmaps Module**: Complete bitmap operations support
  - `redis_bitmap_set_bit_sync` / `redis_bitmap_set_bit_async`: Set bit at offset
  - `redis_bitmap_get_bit_sync` / `redis_bitmap_get_bit_async`: Get bit at offset
  - `redis_bitmap_count_bits_sync` / `redis_bitmap_count_bits_async`: Count set bits
  - `redis_bitmap_get_ttl_sync` / `redis_bitmap_get_ttl_async`: Get TTL
  - `redis_bitmap_extend_ttl_sync` / `redis_bitmap_extend_ttl_async`: Extend TTL
- Examples for bitmaps module in `examples/database/redis/bitmaps/`

---

## [1.5.1] - 2026-04-10

### Fixed
- Alert system API compatibility with new `expression` parameter
- Performance comparison example using `get_stats()` instead of deprecated method
- Reduced package size (42MB → 140KB) by excluding heavy examples

---

## [1.5.0] - 2026-04-10

### Added
- **ParallelExecutor**: Execute pipeline steps in parallel (ThreadPoolExecutor/ProcessPoolExecutor)
- **ExecutionMode**: IO_BOUND, CPU_BOUND, SEQUENTIAL
- **DAGScheduler**: Dependency graph management with topological sorting
- **PipelineAsStep**: Use pipelines as steps in other pipelines
- **@step()** decorator: Inline step definition
- **StepRegistry**: Central registry for decorated steps
- **ResourceMonitor**: Track RAM/CPU during execution
- **Exporter**: JSON/CSV export capabilities
- **Type validators**: Input/output validation

---

## [1.0.0] - 2024-04-01

### Added
- **Pipeline**: Core pipeline orchestration
- **Condition**: Conditional branching based on data
- **Retry**: Automatic retry with backoff
- **APIClient**: External API integration
- **SQLite/Wsqlite**: Data persistence
- **Error handling**: Custom exceptions with codes
- **YAML config**: Load configurations from YAML
- **Nested pipelines**: Compose complex workflows
- **Progress tracking**: Rich terminal output
- **Type hints**: Complete type annotations