# WPipe Changelog

All notable changes to WPipe will be documented in this file.

---

## [0.37.0] - 2026-04-28

### Added
- **Security Pack**: Complete security steps support
  - `fail2ban_check`: Check if IP is banned by Fail2Ban
  - `nmap_scan`: Perform Nmap port scans
  - `shodan_search`: Search host information on Shodan
  - `hash_generator`: Generate cryptographic hashes of strings or files
  - `vault_secrets`: Retrieve secrets from HashiCorp Vault
  - `waf_filter`: Filter strings against SQL Injection and XSS patterns
- Examples for security Steps in `examples/security/`
- Updated README.md with Security Steps inventory
- Updated TODO.txt marking Security pack as completed

---

## [0.36.0] - 2026-04-28

### Added
- **Database Pack**: Complete database steps support
  - `mysql_query`: MySQL/MariaDB SQL query executor
  - `mongo_insert`: MongoDB document inserter
  - `sqlite_audit`: SQLite audit logger
  - `clickhouse_bulk`: ClickHouse bulk data inserter
  - `cassandra_write`: Apache Cassandra data writer
- Pipeline examples for all database Steps in `examples/database/*/`
- Updated README.md with Database Steps inventory
- Updated TODO.txt marking Database pack as completed

---

## [0.35.0] - 2026-04-28

### Added
- **Connectivity Pack**: Complete connectivity steps support
  - `http_request`: HTTP client with automatic retries (GET, POST, PUT, DELETE, PATCH)
  - `graphql_query`: GraphQL query/mutation executor
  - `webhook_trigger`: Webhook notifier
  - `sftp_transfer`: SFTP file transfer (upload/download)
  - `rss_parser`: RSS/Atom feed parser
  - `oauth2_auth`: OAuth2 token manager
- Updated README.md with Connectivity Steps inventory
- Updated TODO.txt marking Connectivity as completed

---

## [0.34.0] - 2026-04-28

### Added
- **Redis Cache Module**: Complete cache decorators support
  - `redis_cache_decorator_sync`: Get cache decorator with TTL
  - `redis_async_cache_decorator`: Get async cache decorator with TTL
  - `redis_retry_decorator_sync`: Get retry decorator with backoff
- Examples for cache module in `examples/database/redis/cache/`

---

## [0.33.0] - 2026-04-28

### Added
- **Redis Pipeline Module**: Complete pipeline operations support
  - `redis_pipeline_execute_sync` / `redis_pipeline_execute_async`: Execute pipeline with multiple commands
- Examples for pipeline module in `examples/database/redis/pipeline/`

---

## [0.32.0] - 2026-04-28

### Added
- **Redis Transactions Module**: Complete transaction operations support
  - `redis_transaction_execute_sync` / `redis_transaction_execute_async`: Execute transaction with multiple commands
- Examples for transactions module in `examples/database/redis/transactions/`

---

## [0.31.0] - 2026-04-28

### Added
- **Redis HyperLogLog Module**: Complete HyperLogLog operations support
  - `redis_hll_add_sync` / `redis_hll_add_async`: Add elements to HyperLogLog
  - `redis_hll_count_sync` / `redis_hll_count_async`: Count unique elements
- Examples for hyperloglog module in `examples/database/redis/hyperloglog/`

---

## [0.30.0] - 2026-04-28

### Added
- **Redis Geo Module**: Complete geo operations support
  - `redis_geo_add_sync` / `redis_geo_add_async`: Add location to geo set
  - `redis_geo_get_distance_sync` / `redis_geo_get_distance_async`: Get distance between members
  - `redis_geo_get_positions_sync` / `redis_geo_get_positions_async`: Get positions of members
  - `redis_geo_search_nearby_sync` / `redis_geo_search_nearby_async`: Search nearby members
  - `redis_geo_search_nearby_dist_sync` / `redis_geo_search_nearby_dist_async`: Search nearby with distance
- Examples for geo module in `examples/database/redis/geo/`

---

## [0.29.0] - 2026-04-28

### Added
- **Redis Streams Module**: Complete streams operations support
  - `redis_stream_add_sync` / `redis_stream_add_async`: Add message to stream
  - `redis_stream_read_sync` / `redis_stream_read_async`: Read messages from stream
  - `redis_stream_on_message_sync` / `redis_stream_on_message_async`: Consume messages with consumer groups
- Examples for streams module in `examples/database/redis/streams/`

---

## [0.28.0] - 2026-04-28

### Added
- **Redis Sorted Sets Module**: Complete sorted sets operations support
  - `redis_sortsets_add_sync` / `redis_sortsets_add_async`: Add member to sorted set
  - `redis_sortsets_get_sync` / `redis_sortsets_get_async`: Get members (ascending)
  - `redis_sortsets_get_reverse_sync` / `redis_sortsets_get_reverse_async`: Get members (descending)
  - `redis_sortsets_remove_sync` / `redis_sortsets_remove_async`: Remove member
  - `redis_sortsets_get_rank_sync` / `redis_sortsets_get_rank_async`: Get rank of member
  - `redis_sortsets_get_score_sync` / `redis_sortsets_get_score_async`: Get score of member
  - `redis_sortsets_increment_score_sync` / `redis_sortsets_increment_score_async`: Increment score
  - `redis_sortsets_get_by_score_sync` / `redis_sortsets_get_by_score_async`: Get by score range
  - `redis_sortsets_delete_sync` / `redis_sortsets_delete_async`: Delete sorted set
  - `redis_sortsets_set_ttl_sync` / `redis_sortsets_set_ttl_async`: Set TTL
  - `redis_sortsets_get_ttl_sync` / `redis_sortsets_get_ttl_async`: Get TTL
- Examples for sortsets module in `examples/database/redis/sortsets/`

---

## [0.27.0] - 2026-04-28

### Added
- **Redis Sets Module**: Complete sets operations support
  - `redis_set_add_sync` / `redis_set_add_async`: Add members to set
  - `redis_set_get_members_sync` / `redis_set_get_members_async`: Get all members
  - `redis_set_is_member_sync` / `redis_set_is_member_async`: Check membership
  - `redis_set_remove_sync` / `redis_set_remove_async`: Remove members
  - `redis_set_get_ttl_sync` / `redis_set_get_ttl_async`: Get TTL
  - `redis_set_extend_ttl_sync` / `redis_set_extend_ttl_async`: Extend TTL
- Examples for sets module in `examples/database/redis/sets/`

---

## [0.26.0] - 2026-04-28

### Added
- **Redis Queue Module**: Complete queue operations support
  - `redis_queue_publish_sync` / `redis_queue_publish_async`: Publish message to queue
  - `redis_queue_on_message_sync` / `redis_queue_on_message_async`: Subscribe to queue
  - `redis_queue_get_length_sync` / `redis_queue_get_length_async`: Get queue length
- Examples for queue module in `examples/database/redis/queue/`

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
- Updated README.md with Redis Steps description

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
- **SQLite/WSQLite**: Data persistence
- **Error handling**: Custom exceptions with codes
- **YAML config**: Load configurations from YAML
- **Nested pipelines**: Compose complex workflows
- **Progress tracking**: Rich terminal output
- **Type hints**: Complete type annotations
