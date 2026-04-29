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
| Step Name | Import | Type | Example | Description |
|-----------|--------|------|---------|-------------|
| `http_request` | `from wpipe_steps.connectivity import HttpRequestStep` | Sync | [http_example.py](examples/connectivity/http_example.py) | HTTP client with GET, POST, PUT, DELETE, PATCH |

### GraphQLQueryStep (package: `wpipe_steps.connectivity`)
| Step Name | Import | Type | Example | Description |
|-----------|--------|------|---------|-------------|
| `graphql_query` | `from wpipe_steps.connectivity import GraphQLQueryStep` | Sync | [graphql_example.py](examples/connectivity/graphql_example.py) | Execute GraphQL queries and mutations |

### WebhookTriggerStep (package: `wpipe_steps.connectivity`)
| Step Name | Import | Type | Example | Description |
|-----------|--------|------|---------|-------------|
| `webhook_trigger` | `from wpipe_steps.connectivity import WebhookTriggerStep` | Sync | [webhook_example.py](examples/connectivity/webhook_example.py) | Send data to external webhooks |

### SftpTransferStep (package: `wpipe_steps.connectivity`)
| Step Name | Import | Type | Example | Description |
|-----------|--------|------|---------|-------------|
| `sftp_transfer` | `from wpipe_steps.connectivity import SftpTransferStep` | Sync | [sftp_example.py](examples/connectivity/sftp_example.py) | Upload/download files via SFTP |

### RSSParserStep (package: `wpipe_steps.connectivity`)
| Step Name | Import | Type | Example | Description |
|-----------|--------|------|---------|-------------|
| `rss_parser` | `from wpipe_steps.connectivity import RSSParserStep` | Sync | [rss_example.py](examples/connectivity/rss_example.py) | Parse RSS/Atom feeds and extract entries |

### OAuth2AuthStep (package: `wpipe_steps.connectivity`)
| Step Name | Import | Type | Example | Description |
|-----------|--------|------|---------|-------------|
| `oauth2_auth` | `from wpipe_steps.connectivity import OAuth2AuthStep` | Sync | [oauth2_example.py](examples/connectivity/oauth2_example.py) | Retrieve and manage OAuth2 access tokens |

---

## 🛡️ Security Steps Inventory

Complete inventory of Security Steps available in `wpipe_steps.security`:

### Fail2Ban (package: `wpipe_steps.security`)
| Step Name | Import | Type | Example | Description |
|-----------|--------|------|---------|-------------|
| `fail2ban_check` | `from wpipe_steps.security import Fail2BanCheckStep` | Sync | [fail2ban_example.py](examples/security/fail2ban_example.py) | Check if IP is banned by Fail2Ban |

### Nmap (package: `wpipe_steps.security`)
| Step Name | Import | Type | Example | Description |
|-----------|--------|------|---------|-------------|
| `nmap_scan` | `from wpipe_steps.security import NmapScanStep` | Sync | [nmap_example.py](examples/security/nmap_example.py) | Perform Nmap port scans |

### Shodan (package: `wpipe_steps.security`)
| Step Name | Import | Type | Example | Description |
|-----------|--------|------|---------|-------------|
| `shodan_search` | `from wpipe_steps.security import ShodanSearchStep` | Sync | [shodan_example.py](examples/security/shodan_example.py) | Search host information on Shodan |

### Hash (package: `wpipe_steps.security`)
| Step Name | Import | Type | Example | Description |
|-----------|--------|------|---------|-------------|
| `hash_generator` | `from wpipe_steps.security import HashGeneratorStep` | Sync | [hash_example.py](examples/security/hash_example.py) | Generate cryptographic hashes of strings or files |

### Vault (package: `wpipe_steps.security`)
| Step Name | Import | Type | Example | Description |
|-----------|--------|------|---------|-------------|
| `vault_secrets` | `from wpipe_steps.security import VaultSecretsStep` | Sync | [vault_example.py](examples/security/vault_example.py) | Retrieve secrets from HashiCorp Vault |

### WAF (package: `wpipe_steps.security`)
| Step Name | Import | Type | Example | Description |
|-----------|--------|------|---------|-------------|
| `waf_filter` | `from wpipe_steps.security import WafFilterStep` | Sync | [waf_example.py](examples/security/waf_example.py) | Filter strings against SQL Injection and XSS patterns |

---

## ☁️ Infrastructure Steps Inventory

Complete inventory of Infrastructure Steps available in `wpipe_steps.infrastructure`:

### S3 (package: `wpipe_steps.infrastructure`)
| Step Name | Import | Type | Example | Description |
|-----------|--------|------|---------|-------------|
| `s3_upload` | `from wpipe_steps.infrastructure import S3BucketUploadStep` | Sync | [s3_example.py](examples/infrastructure/s3_example.py) | Upload files to AWS S3 buckets |

### Docker (package: `wpipe_steps.infrastructure`)
| Step Name | Import | Type | Example | Description |
|-----------|--------|------|---------|-------------|
| `docker_container` | `from wpipe_steps.infrastructure import DockerContainerStep` | Sync | [docker_example.py](examples/infrastructure/docker_example.py) | Manage Docker containers (start, stop, restart) |

### Kubernetes (package: `wpipe_steps.infrastructure`)
| Step Name | Import | Type | Example | Description |
|-----------|--------|------|---------|-------------|
| `kubernetes_pod_check` | `from wpipe_steps.infrastructure import KubernetesPodCheckStep` | Sync | [kubernetes_example.py](examples/infrastructure/kubernetes_example.py) | Monitor the status of a Kubernetes pod |

### Terraform (package: `wpipe_steps.infrastructure`)
| Step Name | Import | Type | Example | Description |
|-----------|--------|------|---------|-------------|
| `terraform_apply` | `from wpipe_steps.infrastructure import TerraformApplyStep` | Sync | [terraform_example.py](examples/infrastructure/terraform_example.py) | Execute Terraform apply for infrastructure changes |

### Proxmox (package: `wpipe_steps.infrastructure`)
| Step Name | Import | Type | Example | Description |
|-----------|--------|------|---------|-------------|
| `proxmox_vm` | `from wpipe_steps.infrastructure import ProxmoxVMStep` | Sync | [proxmox_example.py](examples/infrastructure/proxmox_example.py) | Control virtual machines in Proxmox |

### DigitalOcean (package: `wpipe_steps.infrastructure`)
| Step Name | Import | Type | Example | Description |
|-----------|--------|------|---------|-------------|
| `digitalocean_droplet` | `from wpipe_steps.infrastructure import DigitalOceanDropletStep` | Sync | [digitalocean_example.py](examples/infrastructure/digitalocean_example.py) | Manage DigitalOcean droplets via API |

---

## 📋 Database Steps Inventory

Complete inventory of Database Steps available in `wpipe_steps.database`:

### MySQL (package: `wpipe_steps.database`)
| Step Name | Import | Type | Example | Description |
|-----------|--------|------|---------|-------------|
| `mysql_query` | `from wpipe_steps.database import MySQLQueryStep` | Sync | [example.py](examples/database/mysql/example.py) | Execute SQL queries on MySQL/MariaDB |

### MongoDB (package: `wpipe_steps.database`)
| Step Name | Import | Type | Example | Description |
|-----------|--------|------|---------|-------------|
| `mongo_insert` | `from wpipe_steps.database import MongoInsertStep` | Sync | [example.py](examples/database/mongo/example.py) | Insert documents into MongoDB |

### SQLite (package: `wpipe_steps.database`)
| Step Name | Import | Type | Example | Description |
|-----------|--------|------|---------|-------------|
| `sqlite_audit` | `from wpipe_steps.database import SQLiteAuditStep` | Sync | [example.py](examples/database/sqlite/example.py) | Save audit logs into SQLite |

### ClickHouse (package: `wpipe_steps.database`)
| Step Name | Import | Type | Example | Description |
|-----------|--------|------|---------|-------------|
| `clickhouse_bulk` | `from wpipe_steps.database import ClickHouseBulkStep` | Sync | [example.py](examples/database/clickhouse/example.py) | Bulk insert data into ClickHouse |

### Cassandra (package: `wpipe_steps.database`)
| Step Name | Import | Type | Example | Description |
|-----------|--------|------|---------|-------------|
| `cassandra_write` | `from wpipe_steps.database import CassandraWriteStep` | Sync | [example.py](examples/database/cassandra/example.py) | Write data into Apache Cassandra |

---

## 📋 Redis Steps Inventory

Complete inventory of Redis Steps available in `wpipe_steps.database.redis`:

### Bitmaps (package: `wpipe_steps.database.redis.bitmaps`)
| Step Name | Import | Type | Example | Description |
|-----------|--------|------|---------|-------------|
| `redis_bitmap_set_bit_sync` | `from wpipe_steps.database.redis.bitmaps import redis_bitmap_set_bit_sync` | Sync | [pipeline_sync_example.py](examples/database/redis/bitmaps/pipeline_sync_example.py) | Set a bit at offset in bitmap |
| `redis_bitmap_set_bit_async` | `from wpipe_steps.database.redis.bitmaps import redis_bitmap_set_bit_async` | Async | [pipeline_async_example.py](examples/database/redis/bitmaps/pipeline_async_example.py) | Set a bit at offset in bitmap (async) |
| `redis_bitmap_get_bit_sync` | `from wpipe_steps.database.redis.bitmaps import redis_bitmap_get_bit_sync` | Sync | [pipeline_sync_example.py](examples/database/redis/bitmaps/pipeline_sync_example.py) | Get bit value at offset |
| `redis_bitmap_get_bit_async` | `from wpipe_steps.database.redis.bitmaps import redis_bitmap_get_bit_async` | Async | [pipeline_async_example.py](examples/database/redis/bitmaps/pipeline_async_example.py) | Get bit value at offset (async) |
| `redis_bitmap_count_bits_sync` | `from wpipe_steps.database.redis.bitmaps import redis_bitmap_count_bits_sync` | Sync | [pipeline_sync_example.py](examples/database/redis/bitmaps/pipeline_sync_example.py) | Count set bits in bitmap |
| `redis_bitmap_count_bits_async` | `from wpipe_steps.database.redis.bitmaps import redis_bitmap_count_bits_async` | Async | [pipeline_async_example.py](examples/database/redis/bitmaps/pipeline_async_example.py) | Count set bits in bitmap (async) |
| `redis_bitmap_get_ttl_sync` | `from wpipe_steps.database.redis.bitmaps import redis_bitmap_get_ttl_sync` | Sync | [pipeline_sync_example.py](examples/database/redis/bitmaps/pipeline_sync_example.py) | Get TTL of bitmap key |
| `redis_bitmap_get_ttl_async` | `from wpipe_steps.database.redis.bitmaps import redis_bitmap_get_ttl_async` | Async | [pipeline_async_example.py](examples/database/redis/bitmaps/pipeline_async_example.py) | Get TTL of bitmap key (async) |
| `redis_bitmap_extend_ttl_sync` | `from wpipe_steps.database.redis.bitmaps import redis_bitmap_extend_ttl_sync` | Sync | [pipeline_sync_example.py](examples/database/redis/bitmaps/pipeline_sync_example.py) | Extend TTL of bitmap key |
| `redis_bitmap_extend_ttl_async` | `from wpipe_steps.database.redis.bitmaps import redis_bitmap_extend_ttl_async` | Async | [pipeline_async_example.py](examples/database/redis/bitmaps/pipeline_async_example.py) | Extend TTL of bitmap key (async) |

### Hash (package: `wpipe_steps.database.redis.hash`)
| Step Name | Import | Type | Example | Description |
|-----------|--------|------|---------|-------------|
| `redis_hash_create_sync` | `from wpipe_steps.database.redis.hash import redis_hash_create_sync` | Sync | [pipeline_sync_example.py](examples/database/redis/hash/pipeline_sync_example.py) | Create hash field |
| `redis_hash_create_async` | `from wpipe_steps.database.redis.hash import redis_hash_create_async` | Async | [pipeline_async_example.py](examples/database/redis/hash/pipeline_async_example.py) | Create hash field (async) |
| `redis_hash_read_sync` | `from wpipe_steps.database.redis.hash import redis_hash_read_sync` | Sync | [pipeline_sync_example.py](examples/database/redis/hash/pipeline_sync_example.py) | Read hash field |
| `redis_hash_read_async` | `from wpipe_steps.database.redis.hash import redis_hash_read_async` | Async | [pipeline_async_example.py](examples/database/redis/hash/pipeline_async_example.py) | Read hash field (async) |
| `redis_hash_read_all_sync` | `from wpipe_steps.database.redis.hash import redis_hash_read_all_sync` | Sync | [pipeline_sync_example.py](examples/database/redis/hash/pipeline_sync_example.py) | Read all hash fields |
| `redis_hash_read_all_async` | `from wpipe_steps.database.redis.hash import redis_hash_read_all_async` | Async | [pipeline_async_example.py](examples/database/redis/hash/pipeline_async_example.py) | Read all hash fields (async) |
| `redis_hash_update_sync` | `from wpipe_steps.database.redis.hash import redis_hash_update_sync` | Sync | [pipeline_sync_example.py](examples/database/redis/hash/pipeline_sync_example.py) | Update hash field |
| `redis_hash_update_async` | `from wpipe_steps.database.redis.hash import redis_hash_update_async` | Async | [pipeline_async_example.py](examples/database/redis/hash/pipeline_async_example.py) | Update hash field (async) |
| `redis_hash_delete_sync` | `from wpipe_steps.database.redis.hash import redis_hash_delete_sync` | Sync | [pipeline_sync_example.py](examples/database/redis/hash/pipeline_sync_example.py) | Delete hash field |
| `redis_hash_delete_async` | `from wpipe_steps.database.redis.hash import redis_hash_delete_async` | Async | [pipeline_async_example.py](examples/database/redis/hash/pipeline_async_example.py) | Delete hash field (async) |
| `redis_hash_get_ttl_sync` | `from wpipe_steps.database.redis.hash import redis_hash_get_ttl_sync` | Sync | [pipeline_sync_example.py](examples/database/redis/hash/pipeline_sync_example.py) | Get TTL of hash |
| `redis_hash_get_ttl_async` | `from wpipe_steps.database.redis.hash import redis_hash_get_ttl_async` | Async | [pipeline_async_example.py](examples/database/redis/hash/pipeline_async_example.py) | Get TTL of hash (async) |
| `redis_hash_extend_ttl_sync` | `from wpipe_steps.database.redis.hash import redis_hash_extend_ttl_sync` | Sync | [pipeline_sync_example.py](examples/database/redis/hash/pipeline_sync_example.py) | Extend TTL of hash |
| `redis_hash_extend_ttl_async` | `from wpipe_steps.database.redis.hash import redis_hash_extend_ttl_async` | Async | [pipeline_async_example.py](examples/database/redis/hash/pipeline_async_example.py) | Extend TTL of hash (async) |

### Pub/Sub (package: `wpipe_steps.database.redis.pubsub`)
| Step Name | Import | Type | Example | Description |
|-----------|--------|------|---------|-------------|
| `redis_pubsub_publish_sync` | `from wpipe_steps.database.redis.pubsub import redis_pubsub_publish_sync` | Sync | [pipeline_sync_example.py](examples/database/redis/pubsub/pipeline_sync_example.py) | Publish message to channel |
| `redis_pubsub_publish_async` | `from wpipe_steps.database.redis.pubsub import redis_pubsub_publish_async` | Async | [pipeline_async_example.py](examples/database/redis/pubsub/pipeline_async_example.py) | Publish message to channel (async) |
| `redis_pubsub_on_message_sync` | `from wpipe_steps.database.redis.pubsub import redis_pubsub_on_message_sync` | Sync | [pipeline_sync_example.py](examples/database/redis/pubsub/pipeline_sync_example.py) | Subscribe to channel (returns decorator) |
| `redis_pubsub_on_message_async` | `from wpipe_steps.database.redis.pubsub import redis_pubsub_on_message_async` | Async | [pipeline_async_example.py](examples/database/redis/pubsub/pipeline_async_example.py) | Subscribe to channel (async, returns decorator) |

### Queue (package: `wpipe_steps.database.redis.queue`)
| Step Name | Import | Type | Example | Description |
|-----------|--------|------|---------|-------------|
| `redis_queue_publish_sync` | `from wpipe_steps.database.redis.queue import redis_queue_publish_sync` | Sync | [pipeline_sync_example.py](examples/database/redis/queue/pipeline_sync_example.py) | Publish message to queue |
| `redis_queue_publish_async` | `from wpipe_steps.database.redis.queue import redis_queue_publish_async` | Async | [pipeline_async_example.py](examples/database/redis/queue/pipeline_async_example.py) | Publish message to queue (async) |
| `redis_queue_on_message_sync` | `from wpipe_steps.database.redis.queue import redis_queue_on_message_sync` | Sync | [pipeline_sync_example.py](examples/database/redis/queue/pipeline_sync_example.py) | Subscribe to queue (returns decorator) |
| `redis_queue_on_message_async` | `from wpipe_steps.database.redis.queue import redis_queue_on_message_async` | Async | [pipeline_async_example.py](examples/database/redis/queue/pipeline_async_example.py) | Subscribe to queue (async, returns decorator) |
| `redis_queue_get_length_sync` | `from wpipe_steps.database.redis.queue import redis_queue_get_length_sync` | Sync | [pipeline_sync_example.py](examples/database/redis/queue/pipeline_sync_example.py) | Get queue length |
| `redis_queue_get_length_async` | `from wpipe_steps.database.redis.queue import redis_queue_get_length_async` | Async | [pipeline_async_example.py](examples/database/redis/queue/pipeline_async_example.py) | Get queue length (async) |

### Sets (package: `wpipe_steps.database.redis.sets`)
| Step Name | Import | Type | Example | Description |
|-----------|--------|------|---------|-------------|
| `redis_set_add_sync` | `from wpipe_steps.database.redis.sets import redis_set_add_sync` | Sync | [pipeline_sync_example.py](examples/database/redis/sets/pipeline_sync_example.py) | Add members to set |
| `redis_set_add_async` | `from wpipe_steps.database.redis.sets import redis_set_add_async` | Async | [pipeline_async_example.py](examples/database/redis/sets/pipeline_async_example.py) | Add members to set (async) |
| `redis_set_get_members_sync` | `from wpipe_steps.database.redis.sets import redis_set_get_members_sync` | Sync | [pipeline_sync_example.py](examples/database/redis/sets/pipeline_sync_example.py) | Get all members from set |
| `redis_set_get_members_async` | `from wpipe_steps.database.redis.sets import redis_set_get_members_async` | Async | [pipeline_async_example.py](examples/database/redis/sets/pipeline_async_example.py) | Get all members from set (async) |
| `redis_set_is_member_sync` | `from wpipe_steps.database.redis.sets import redis_set_is_member_sync` | Sync | [pipeline_sync_example.py](examples/database/redis/sets/pipeline_sync_example.py) | Check membership in set |
| `redis_set_is_member_async` | `from wpipe_steps.database.redis.sets import redis_set_is_member_async` | Async | [pipeline_async_example.py](examples/database/redis/sets/pipeline_async_example.py) | Check membership in set (async) |
| `redis_set_remove_sync` | `from wpipe_steps.database.redis.sets import redis_set_remove_sync` | Sync | [pipeline_sync_example.py](examples/database/redis/sets/pipeline_sync_example.py) | Remove members from set |
| `redis_set_remove_async` | `from wpipe_steps.database.redis.sets import redis_set_remove_async` | Async | [pipeline_async_example.py](examples/database/redis/sets/pipeline_async_example.py) | Remove members from set (async) |
| `redis_set_get_ttl_sync` | `from wpipe_steps.database.redis.sets import redis_set_get_ttl_sync` | Sync | [pipeline_sync_example.py](examples/database/redis/sets/pipeline_sync_example.py) | Get TTL of set |
| `redis_set_get_ttl_async` | `from wpipe_steps.database.redis.sets import redis_set_get_ttl_async` | Async | [pipeline_async_example.py](examples/database/redis/sets/pipeline_async_example.py) | Get TTL of set (async) |
| `redis_set_extend_ttl_sync` | `from wpipe_steps.database.redis.sets import redis_set_extend_ttl_sync` | Sync | [pipeline_sync_example.py](examples/database/redis/sets/pipeline_sync_example.py) | Extend TTL of set |
| `redis_set_extend_ttl_async` | `from wpipe_steps.database.redis.sets import redis_set_extend_ttl_async` | Async | [pipeline_async_example.py](examples/database/redis/sets/pipeline_async_example.py) | Extend TTL of set (async) |

### Sorted Sets (package: `wpipe_steps.database.redis.sortsets`)
| Step Name | Import | Type | Example | Description |
|-----------|--------|------|---------|-------------|
| `redis_sortsets_add_sync` | `from wpipe_steps.database.redis.sortsets import redis_sortsets_add_sync` | Sync | [pipeline_sync_example.py](examples/database/redis/sortsets/pipeline_sync_example.py) | Add member to sorted set |
| `redis_sortsets_add_async` | `from wpipe_steps.database.redis.sortsets import redis_sortsets_add_async` | Async | [pipeline_async_example.py](examples/database/redis/sortsets/pipeline_async_example.py) | Add member to sorted set (async) |
| `redis_sortsets_get_sync` | `from wpipe_steps.database.redis.sortsets import redis_sortsets_get_sync` | Sync | [pipeline_sync_example.py](examples/database/redis/sortsets/pipeline_sync_example.py) | Get members (ascending) |
| `redis_sortsets_get_async` | `from wpipe_steps.database.redis.sortsets import redis_sortsets_get_async` | Async | [pipeline_async_example.py](examples/database/redis/sortsets/pipeline_async_example.py) | Get members (ascending, async) |
| `redis_sortsets_get_reverse_sync` | `from wpipe_steps.database.redis.sortsets import redis_sortsets_get_reverse_sync` | Sync | [pipeline_sync_example.py](examples/database/redis/sortsets/pipeline_sync_example.py) | Get members (descending) |
| `redis_sortsets_get_reverse_async` | `from wpipe_steps.database.redis.sortsets import redis_sortsets_get_reverse_async` | Async | [pipeline_async_example.py](examples/database/redis/sortsets/pipeline_async_example.py) | Get members (descending, async) |
| `redis_sortsets_remove_sync` | `from wpipe_steps.database.redis.sortsets import redis_sortsets_remove_sync` | Sync | [pipeline_sync_example.py](examples/database/redis/sortsets/pipeline_sync_example.py) | Remove member from sorted set |
| `redis_sortsets_remove_async` | `from wpipe_steps.database.redis.sortsets import redis_sortsets_remove_async` | Async | [pipeline_async_example.py](examples/database/redis/sortsets/pipeline_async_example.py) | Remove member from sorted set (async) |
| `redis_sortsets_get_rank_sync` | `from wpipe_steps.database.redis.sortsets import redis_sortsets_get_rank_sync` | Sync | [pipeline_sync_example.py](examples/database/redis/sortsets/pipeline_sync_example.py) | Get rank of member |
| `redis_sortsets_get_rank_async` | `from wpipe_steps.database.redis.sortsets import redis_sortsets_get_rank_async` | Async | [pipeline_async_example.py](examples/database/redis/sortsets/pipeline_async_example.py) | Get rank of member (async) |
| `redis_sortsets_get_score_sync` | `from wpipe_steps.database.redis.sortsets import redis_sortsets_get_score_sync` | Sync | [pipeline_sync_example.py](examples/database/redis/sortsets/pipeline_sync_example.py) | Get score of member |
| `redis_sortsets_get_score_async` | `from wpipe_steps.database.redis.sortsets import redis_sortsets_get_score_async` | Async | [pipeline_async_example.py](examples/database/redis/sortsets/pipeline_async_example.py) | Get score of member (async) |
| `redis_sortsets_increment_score_sync` | `from wpipe_steps.database.redis.sortsets import redis_sortsets_increment_score_sync` | Sync | [pipeline_sync_example.py](examples/database/redis/sortsets/pipeline_sync_example.py) | Increment score of member |
| `redis_sortsets_increment_score_async` | `from wpipe_steps.database.redis.sortsets import redis_sortsets_increment_score_async` | Async | [pipeline_async_example.py](examples/database/redis/sortsets/pipeline_async_example.py) | Increment score of member (async) |
| `redis_sortsets_get_by_score_sync` | `from wpipe_steps.database.redis.sortsets import redis_sortsets_get_by_score_sync` | Sync | [pipeline_sync_example.py](examples/database/redis/sortsets/pipeline_sync_example.py) | Get members by score range |
| `redis_sortsets_get_by_score_async` | `from wpipe_steps.database.redis.sortsets import redis_sortsets_get_by_score_async` | Async | [pipeline_async_example.py](examples/database/redis/sortsets/pipeline_async_example.py) | Get members by score range (async) |
| `redis_sortsets_delete_sync` | `from wpipe_steps.database.redis.sortsets import redis_sortsets_delete_sync` | Sync | [pipeline_sync_example.py](examples/database/redis/sortsets/pipeline_sync_example.py) | Delete sorted set |
| `redis_sortsets_delete_async` | `from wpipe_steps.database.redis.sortsets import redis_sortsets_delete_async` | Async | [pipeline_async_example.py](examples/database/redis/sortsets/pipeline_async_example.py) | Delete sorted set (async) |
| `redis_sortsets_set_ttl_sync` | `from wpipe_steps.database.redis.sortsets import redis_sortsets_set_ttl_sync` | Sync | [pipeline_sync_example.py](examples/database/redis/sortsets/pipeline_sync_example.py) | Set TTL of sorted set |
| `redis_sortsets_set_ttl_async` | `from wpipe_steps.database.redis.sortsets import redis_sortsets_set_ttl_async` | Async | [pipeline_async_example.py](examples/database/redis/sortsets/pipeline_async_example.py) | Set TTL of sorted set (async) |
| `redis_sortsets_get_ttl_sync` | `from wpipe_steps.database.redis.sortsets import redis_sortsets_get_ttl_sync` | Sync | [pipeline_sync_example.py](examples/database/redis/sortsets/pipeline_sync_example.py) | Get TTL of sorted set |
| `redis_sortsets_get_ttl_async` | `from wpipe_steps.database.redis.sortsets import redis_sortsets_get_ttl_async` | Async | [pipeline_async_example.py](examples/database/redis/sortsets/pipeline_async_example.py) | Get TTL of sorted set (async) |

### Streams (package: `wpipe_steps.database.redis.streams`)
| Step Name | Import | Type | Example | Description |
|-----------|--------|------|---------|-------------|
| `redis_stream_add_sync` | `from wpipe_steps.database.redis.streams import redis_stream_add_sync` | Sync | [pipeline_sync_example.py](examples/database/redis/streams/pipeline_sync_example.py) | Add message to stream |
| `redis_stream_add_async` | `from wpipe_steps.database.redis.streams import redis_stream_add_async` | Async | [pipeline_async_example.py](examples/database/redis/streams/pipeline_async_example.py) | Add message to stream (async) |
| `redis_stream_read_sync` | `from wpipe_steps.database.redis.streams import redis_stream_read_sync` | Sync | [pipeline_sync_example.py](examples/database/redis/streams/pipeline_sync_example.py) | Read messages from stream |
| `redis_stream_read_async` | `from wpipe_steps.database.redis.streams import redis_stream_read_async` | Async | [pipeline_async_example.py](examples/database/redis/streams/pipeline_async_example.py) | Read messages from stream (async) |
| `redis_stream_on_message_sync` | `from wpipe_steps.database.redis.streams import redis_stream_on_message_sync` | Sync | [pipeline_sync_example.py](examples/database/redis/streams/pipeline_sync_example.py) | Consume messages with consumer group (returns decorator) |
| `redis_stream_on_message_async` | `from wpipe_steps.database.redis.streams import redis_stream_on_message_async` | Async | [pipeline_async_example.py](examples/database/redis/streams/pipeline_async_example.py) | Consume messages with consumer group (async, returns decorator) |

### Geo (package: `wpipe_steps.database.redis.geo`)
| Step Name | Import | Type | Example | Description |
|-----------|--------|------|---------|-------------|
| `redis_geo_add_sync` | `from wpipe_steps.database.redis.geo import redis_geo_add_sync` | Sync | [pipeline_sync_example.py](examples/database/redis/geo/pipeline_sync_example.py) | Add location to geo set |
| `redis_geo_add_async` | `from wpipe_steps.database.redis.geo import redis_geo_add_async` | Async | [pipeline_async_example.py](examples/database/redis/geo/pipeline_async_example.py) | Add location to geo set (async) |
| `redis_geo_get_distance_sync` | `from wpipe_steps.database.redis.geo import redis_geo_get_distance_sync` | Sync | [pipeline_sync_example.py](examples/database/redis/geo/pipeline_sync_example.py) | Get distance between members |
| `redis_geo_get_distance_async` | `from wpipe_steps.database.redis.geo import redis_geo_get_distance_async` | Async | [pipeline_async_example.py](examples/database/redis/geo/pipeline_async_example.py) | Get distance between members (async) |
| `redis_geo_get_positions_sync` | `from wpipe_steps.database.redis.geo import redis_geo_get_positions_sync` | Sync | [pipeline_sync_example.py](examples/database/redis/geo/pipeline_sync_example.py) | Get positions of members |
| `redis_geo_get_positions_async` | `from wpipe_steps.database.redis.geo import redis_geo_get_positions_async` | Async | [pipeline_async_example.py](examples/database/redis/geo/pipeline_async_example.py) | Get positions of members (async) |
| `redis_geo_search_nearby_sync` | `from wpipe_steps.database.redis.geo import redis_geo_search_nearby_sync` | Sync | [pipeline_sync_example.py](examples/database/redis/geo/pipeline_sync_example.py) | Search nearby members |
| `redis_geo_search_nearby_async` | `from wpipe_steps.database.redis.geo import redis_geo_search_nearby_async` | Async | [pipeline_async_example.py](examples/database/redis/geo/pipeline_async_example.py) | Search nearby members (async) |
| `redis_geo_search_nearby_dist_sync` | `from wpipe_steps.database.redis.geo import redis_geo_search_nearby_dist_sync` | Sync | [pipeline_sync_example.py](examples/database/redis/geo/pipeline_sync_example.py) | Search nearby with distance |
| `redis_geo_search_nearby_dist_async` | `from wpipe_steps.database.redis.geo import redis_geo_search_nearby_dist_async` | Async | [pipeline_async_example.py](examples/database/redis/geo/pipeline_async_example.py) | Search nearby with distance (async) |

### HyperLogLog (package: `wpipe_steps.database.redis.hyperloglog`)
| Step Name | Import | Type | Example | Description |
|-----------|--------|------|---------|-------------|
| `redis_hll_add_sync` | `from wpipe_steps.database.redis.hyperloglog import redis_hll_add_sync` | Sync | [pipeline_sync_example.py](examples/database/redis/hyperloglog/pipeline_sync_example.py) | Add elements to HyperLogLog |
| `redis_hll_add_async` | `from wpipe_steps.database.redis.hyperloglog import redis_hll_add_async` | Async | [pipeline_async_example.py](examples/database/redis/hyperloglog/pipeline_async_example.py) | Add elements to HyperLogLog (async) |
| `redis_hll_count_sync` | `from wpipe_steps.database.redis.hyperloglog import redis_hll_count_sync` | Sync | [pipeline_sync_example.py](examples/database/redis/hyperloglog/pipeline_sync_example.py) | Count unique elements |
| `redis_hll_count_async` | `from wpipe_steps.database.redis.hyperloglog import redis_hll_count_async` | Async | [pipeline_async_example.py](examples/database/redis/hyperloglog/pipeline_async_example.py) | Count unique elements (async) |

### Transactions (package: `wpipe_steps.database.redis.transactions`)
| Step Name | Import | Type | Example | Description |
|-----------|--------|------|---------|-------------|
| `redis_transaction_execute_sync` | `from wpipe_steps.database.redis.transactions import redis_transaction_execute_sync` | Sync | [pipeline_sync_example.py](examples/database/redis/transactions/pipeline_sync_example.py) | Execute transaction with multiple commands |
| `redis_transaction_execute_async` | `from wpipe_steps.database.redis.transactions import redis_transaction_execute_async` | Async | [pipeline_async_example.py](examples/database/redis/transactions/pipeline_async_example.py) | Execute transaction with multiple commands (async) |

### Pipeline (package: `wpipe_steps.database.redis.pipeline`)
| Step Name | Import | Type | Example | Description |
|-----------|--------|------|---------|-------------|
| `redis_pipeline_execute_sync` | `from wpipe_steps.database.redis.pipeline import redis_pipeline_execute_sync` | Sync | [pipeline_sync_example.py](examples/database/redis/pipeline/pipeline_sync_example.py) | Execute pipeline with multiple commands |
| `redis_pipeline_execute_async` | `from wpipe_steps.database.redis.pipeline import redis_pipeline_execute_async` | Async | [pipeline_async_example.py](examples/database/redis/pipeline/pipeline_async_example.py) | Execute pipeline with multiple commands (async) |

### Cache Decorators (package: `wpipe_steps.database.redis.cache`)
| Step Name | Import | Type | Example | Description |
|-----------|--------|------|---------|-------------|
| `redis_cache_decorator_sync` | `from wpipe_steps.database.redis.cache import redis_cache_decorator_sync` | Sync | [pipeline_sync_example.py](examples/database/redis/cache/pipeline_sync_example.py) | Get cache decorator with TTL |
| `redis_async_cache_decorator` | `from wpipe_steps.database.redis.cache import redis_async_cache_decorator` | Async | [pipeline_async_example.py](examples/database/redis/cache/pipeline_async_example.py) | Get async cache decorator with TTL |
| `redis_retry_decorator_sync` | `from wpipe_steps.database.redis.cache import redis_retry_decorator_sync` | Sync | [pipeline_sync_example.py](examples/database/redis/cache/pipeline_sync_example.py) | Get retry decorator with backoff |

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
### System (package: `wpipe_steps.system`)| Step Name | Import | Type | Example | Description ||-----------|--------|------|---------|-------------|| `cpu_monitor` | `from wpipe_steps.system import CpuMonitorStep` | Sync | [cpu_monitor_example.py](examples/system/cpu_monitor/cpu_monitor_example.py) | Obtener carga del sistema antes de procesos pesados. || `cpu_monitor` | `from wpipe_steps.system import CpuMonitorStep` | Sync | [cpu_monitor_example.py](examples/system/cpu_monitor/cpu_monitor_example.py) | Obtener carga del sistema antes de procesos pesados. |
| `shell_exec` | `from wpipe_steps.system import ShellExecStep` | Sync | [shell_exec_example.py](examples/system/shell_exec/shell_exec_example.py) | Ejecución controlada de comandos Bash/PowerShell. |
| `disk_space_check` | `from wpipe_steps.system import DiskSpaceCheckStep` | Sync | [disk_space_check_example.py](examples/system/disk_space_check/disk_space_check_example.py) | Alerta si queda poco espacio para el proceso. |
| `health_check` | `from wpipe_steps.system import HealthCheckStep` | Sync | [health_check_example.py](examples/system/health_check/health_check_example.py) | Ping a una lista de servicios críticos. |
