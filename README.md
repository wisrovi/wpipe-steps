# 🧱 WPipe Steps

**A professional collection of pre-built, production-ready steps and states for the WPipe orchestration engine.**

WPipe Steps provides a comprehensive library of modular components ("Steps") that can be easily integrated into your WPipe pipelines. Instead of reinventing the wheel for common tasks like API calls, database queries, or notifications, simply import and use a pre-built step.

---

## 📂 Professional Structure

The library is organized into logical "Packs" based on functionality:

| Pack | Namespace | Description |
|------|-----------|-------------|
| 🌐 **Connectivity** | `wpipe_steps.connectivity` | **HttpRequestStep**: REST client with automatic retries. <br> **GraphQLQueryStep**: GraphQL executor. <br> **WebhookTriggerStep**: Webhook notifier. <br> **SftpTransferStep**: SFTP transfer (upload/download). <br> **RSSParserStep**: RSS/Atom feed parser. <br> **OAuth2AuthStep**: OAuth2 token manager. |
| 📊 **Database** | `wpipe_steps.database` | **MySQLQueryStep**: MySQL SQL executor. <br> **Redis Steps**: Full Redis support via wredis (bitmaps, hash, sets, sorted sets, streams, pub/sub, queue, geo, hyperloglog, transactions, pipeline, cache decorators) - sync/async. <br> **MongoInsertStep**: MongoDB document inserter. <br> **SQLiteAuditStep**: Local SQLite audit logger. <br> **ClickHouseBulkStep**: ClickHouse massive data inserter. <br> **CassandraWriteStep**: Cassandra data writer. |
| 🛡️ **Security** | `wpipe_steps.security` | **Fail2BanCheckStep**: IP ban status verifier. <br> **NmapScanStep**: Port scanning discovery. <br> **ShodanSearchStep**: Network intelligence search. <br> **HashGeneratorStep**: Hash generator. <br> **VaultSecretsStep**: Vault secrets retriever. <br> **WafFilterStep**: SQLi/XSS input filter. |
| ☁️ **Infrastructure** | `wpipe_steps.infrastructure` | **S3BucketUploadStep**: AWS S3 file uploader. |
| 📧 **Communication** | `wpipe_steps.communication` | Telegram, Slack, Discord, SendGrid, Twilio. |
| 📁 **Data** | `wpipe_steps.data` | CSV, JSON, PDF, Excel, Image Processing. |
| 🎙️ **Multimedia** | `wpipe_steps.multimedia` | Audio Normalization, Whisper AI, TTS. |
| 🤖 **AI** | `wpipe_steps.ai` | OpenAI, HuggingFace, Sentiment Analysis. |
| ⚙️ **System** | `wpipe_steps.system` | Resource Monitoring, Shell Exec, Health Checks. |

---

## 📋 Connectivity Steps Inventory

Complete inventory of Connectivity Steps available in `wpipe_steps.connectivity`:

### HttpRequestStep (package: `wpipe_steps.connectivity`)
| Step Name | Type | Description |
|-----------|------|-------------|
| `http_request` | Sync | HTTP client with GET, POST, PUT, DELETE, PATCH |

### GraphQLQueryStep (package: `wpipe_steps.connectivity`)
| Step Name | Type | Description |
|-----------|------|-------------|
| `graphql_query` | Sync | Execute GraphQL queries and mutations |

### WebhookTriggerStep (package: `wpipe_steps.connectivity`)
| Step Name | Type | Description |
|-----------|------|-------------|
| `webhook_trigger` | Sync | Send data to external webhooks |

### SftpTransferStep (package: `wpipe_steps.connectivity`)
| Step Name | Type | Description |
|-----------|------|-------------|
| `sftp_transfer` | Sync | Upload/download files via SFTP |

### RSSParserStep (package: `wpipe_steps.connectivity`)
| Step Name | Type | Description |
|-----------|------|-------------|
| `rss_parser` | Sync | Parse RSS/Atom feeds and extract entries |

### OAuth2AuthStep (package: `wpipe_steps.connectivity`)
| Step Name | Type | Description |
|-----------|------|-------------|
| `oauth2_auth` | Sync | Retrieve and manage OAuth2 access tokens |

---

## 📋 Redis Steps Inventory

Complete inventory of Redis Steps available in `wpipe_steps.database.redis`:

### Bitmaps (package: `wpipe_steps.database.redis.bitmaps`)
| Step Name | Type | Description |
|-----------|------|-------------|
| `redis_bitmap_set_bit_sync` | Sync | Set a bit at offset in bitmap |
| `redis_bitmap_set_bit_async` | Async | Set a bit at offset in bitmap (async) |
| `redis_bitmap_get_bit_sync` | Sync | Get bit value at offset |
| `redis_bitmap_get_bit_async` | Async | Get bit value at offset (async) |
| `redis_bitmap_count_bits_sync` | Sync | Count set bits in bitmap |
| `redis_bitmap_count_bits_async` | Async | Count set bits in bitmap (async) |
| `redis_bitmap_get_ttl_sync` | Sync | Get TTL of bitmap key |
| `redis_bitmap_get_ttl_async` | Async | Get TTL of bitmap key (async) |
| `redis_bitmap_extend_ttl_sync` | Sync | Extend TTL of bitmap key |
| `redis_bitmap_extend_ttl_async` | Async | Extend TTL of bitmap key (async) |

### Hash (package: `wpipe_steps.database.redis.hash`)
| Step Name | Type | Description |
|-----------|------|-------------|
| `redis_hash_create_sync` | Sync | Create hash field |
| `redis_hash_create_async` | Async | Create hash field (async) |
| `redis_hash_read_sync` | Sync | Read hash field |
| `redis_hash_read_async` | Async | Read hash field (async) |
| `redis_hash_read_all_sync` | Sync | Read all hash fields |
| `redis_hash_read_all_async` | Async | Read all hash fields (async) |
| `redis_hash_update_sync` | Sync | Update hash field |
| `redis_hash_update_async` | Async | Update hash field (async) |
| `redis_hash_delete_sync` | Sync | Delete hash field |
| `redis_hash_delete_async` | Async | Delete hash field (async) |
| `redis_hash_get_ttl_sync` | Sync | Get TTL of hash |
| `redis_hash_get_ttl_async` | Async | Get TTL of hash (async) |
| `redis_hash_extend_ttl_sync` | Sync | Extend TTL of hash |
| `redis_hash_extend_ttl_async` | Async | Extend TTL of hash (async) |

### Pub/Sub (package: `wpipe_steps.database.redis.pubsub`)
| Step Name | Type | Description |
|-----------|------|-------------|
| `redis_pubsub_publish_sync` | Sync | Publish message to channel |
| `redis_pubsub_publish_async` | Async | Publish message to channel (async) |
| `redis_pubsub_on_message_sync` | Sync | Subscribe to channel (returns decorator) |
| `redis_pubsub_on_message_async` | Async | Subscribe to channel (async, returns decorator) |

### Queue (package: `wpipe_steps.database.redis.queue`)
| Step Name | Type | Description |
|-----------|------|-------------|
| `redis_queue_publish_sync` | Sync | Publish message to queue |
| `redis_queue_publish_async` | Async | Publish message to queue (async) |
| `redis_queue_on_message_sync` | Sync | Subscribe to queue (returns decorator) |
| `redis_queue_on_message_async` | Async | Subscribe to queue (async, returns decorator) |
| `redis_queue_get_length_sync` | Sync | Get queue length |
| `redis_queue_get_length_async` | Async | Get queue length (async) |

### Sets (package: `wpipe_steps.database.redis.sets`)
| Step Name | Type | Description |
|-----------|------|-------------|
| `redis_set_add_sync` | Sync | Add members to set |
| `redis_set_add_async` | Async | Add members to set (async) |
| `redis_set_get_members_sync` | Sync | Get all members from set |
| `redis_set_get_members_async` | Async | Get all members from set (async) |
| `redis_set_is_member_sync` | Sync | Check membership in set |
| `redis_set_is_member_async` | Async | Check membership in set (async) |
| `redis_set_remove_sync` | Sync | Remove members from set |
| `redis_set_remove_async` | Async | Remove members from set (async) |
| `redis_set_get_ttl_sync` | Sync | Get TTL of set |
| `redis_set_get_ttl_async` | Async | Get TTL of set (async) |
| `redis_set_extend_ttl_sync` | Sync | Extend TTL of set |
| `redis_set_extend_ttl_async` | Async | Extend TTL of set (async) |

### Sorted Sets (package: `wpipe_steps.database.redis.sortsets`)
| Step Name | Type | Description |
|-----------|------|-------------|
| `redis_sortsets_add_sync` | Sync | Add member to sorted set |
| `redis_sortsets_add_async` | Async | Add member to sorted set (async) |
| `redis_sortsets_get_sync` | Sync | Get members (ascending) |
| `redis_sortsets_get_async` | Async | Get members (ascending, async) |
| `redis_sortsets_get_reverse_sync` | Sync | Get members (descending) |
| `redis_sortsets_get_reverse_async` | Async | Get members (descending, async) |
| `redis_sortsets_remove_sync` | Sync | Remove member from sorted set |
| `redis_sortsets_remove_async` | Async | Remove member from sorted set (async) |
| `redis_sortsets_get_rank_sync` | Sync | Get rank of member |
| `redis_sortsets_get_rank_async` | Async | Get rank of member (async) |
| `redis_sortsets_get_score_sync` | Sync | Get score of member |
| `redis_sortsets_get_score_async` | Async | Get score of member (async) |
| `redis_sortsets_increment_score_sync` | Sync | Increment score of member |
| `redis_sortsets_increment_score_async` | Async | Increment score of member (async) |
| `redis_sortsets_get_by_score_sync` | Sync | Get members by score range |
| `redis_sortsets_get_by_score_async` | Async | Get members by score range (async) |
| `redis_sortsets_delete_sync` | Sync | Delete sorted set |
| `redis_sortsets_delete_async` | Async | Delete sorted set (async) |
| `redis_sortsets_set_ttl_sync` | Sync | Set TTL of sorted set |
| `redis_sortsets_set_ttl_async` | Async | Set TTL of sorted set (async) |
| `redis_sortsets_get_ttl_sync` | Sync | Get TTL of sorted set |
| `redis_sortsets_get_ttl_async` | Async | Get TTL of sorted set (async) |

### Streams (package: `wpipe_steps.database.redis.streams`)
| Step Name | Type | Description |
|-----------|------|-------------|
| `redis_stream_add_sync` | Sync | Add message to stream |
| `redis_stream_add_async` | Async | Add message to stream (async) |
| `redis_stream_read_sync` | Sync | Read messages from stream |
| `redis_stream_read_async` | Async | Read messages from stream (async) |
| `redis_stream_on_message_sync` | Sync | Consume messages with consumer group (returns decorator) |
| `redis_stream_on_message_async` | Async | Consume messages with consumer group (async, returns decorator) |

### Geo (package: `wpipe_steps.database.redis.geo`)
| Step Name | Type | Description |
|-----------|------|-------------|
| `redis_geo_add_sync` | Sync | Add location to geo set |
| `redis_geo_add_async` | Async | Add location to geo set (async) |
| `redis_geo_get_distance_sync` | Sync | Get distance between members |
| `redis_geo_get_distance_async` | Async | Get distance between members (async) |
| `redis_geo_get_positions_sync` | Sync | Get positions of members |
| `redis_geo_get_positions_async` | Async | Get positions of members (async) |
| `redis_geo_search_nearby_sync` | Sync | Search nearby members |
| `redis_geo_search_nearby_async` | Async | Search nearby members (async) |
| `redis_geo_search_nearby_dist_sync` | Sync | Search nearby with distance |
| `redis_geo_search_nearby_dist_async` | Async | Search nearby with distance (async) |

### HyperLogLog (package: `wpipe_steps.database.redis.hyperloglog`)
| Step Name | Type | Description |
|-----------|------|-------------|
| `redis_hll_add_sync` | Sync | Add elements to HyperLogLog |
| `redis_hll_add_async` | Async | Add elements to HyperLogLog (async) |
| `redis_hll_count_sync` | Sync | Count unique elements |
| `redis_hll_count_async` | Async | Count unique elements (async) |

### Transactions (package: `wpipe_steps.database.redis.transactions`)
| Step Name | Type | Description |
|-----------|------|-------------|
| `redis_transaction_execute_sync` | Sync | Execute transaction with multiple commands |
| `redis_transaction_execute_async` | Async | Execute transaction with multiple commands (async) |

### Pipeline (package: `wpipe_steps.database.redis.pipeline`)
| Step Name | Type | Description |
|-----------|------|-------------|
| `redis_pipeline_execute_sync` | Sync | Execute pipeline with multiple commands |
| `redis_pipeline_execute_async` | Async | Execute pipeline with multiple commands (async) |

### Cache Decorators (package: `wpipe_steps.database.redis.cache`)
| Step Name | Type | Description |
|-----------|------|-------------|
| `redis_cache_decorator_sync` | Sync | Get cache decorator with TTL |
| `redis_async_cache_decorator` | Async | Get async cache decorator with TTL |
| `redis_retry_decorator_sync` | Sync | Get retry decorator with backoff |

---

## 🚀 Quick Start

### Installation
```bash
pip install wpipe-steps
```

### Basic Usage
```python
from wpipe import Pipeline
from wpipe_steps.connectivity import HttpRequestStep

# Create a pipeline
pipeline = Pipeline(pipeline_name="fetch_api")

# Use a pre-built step
pipeline.set_steps([
    HttpRequestStep.as_step(
        name="fetch_user",
        url="https://api.example.com/user/1",
        method="GET"
    )
])

pipeline.run({})
```

---

## 🛠️ Developer Guide: Creating a New Step

All steps should inherit from `BaseStep` located in `wpipe_steps.core.base`.

```python
from wpipe_steps.core.base import BaseStep

class MyCustomStep(BaseStep):
    def execute(self, data):
        # Your logic here
        data["my_key"] = "my_value"
        return data
```

---

## 📢 Roadmap

Check the [TODO.txt](./TODO.txt) for the full list of planned steps for each pack.

---

Diseñado con ❤️ por **William Rodriguez** (wisrovi) para ingenieros que buscan máxima productividad.
