# 📊 Database Examples

This directory contains examples of how to interact with different databases using pre-built steps.

## Examples included:

### 1. MySQL/MariaDB (`mysql_example.py`)
Shows how to execute SQL queries (SELECT, INSERT, etc.) on MySQL databases using `MySQLQueryStep`.

### 2. Redis Cache (`redis_example.py`)
Demonstrates how to store and retrieve data from Redis using `RedisCacheStep`.

### 3. MongoDB Insert (`mongodb_example.py`)
Demonstrates how to insert documents into MongoDB collections using `MongoInsertStep`.

### 4. SQLite Audit (`sqlite_example.py`)
Demonstrates how to save local audit logs and data snapshots into a SQLite database using `SQLiteAuditStep`.

### 5. ClickHouse Bulk (`clickhouse_example.py`)
Demonstrates how to perform massive data insertions into ClickHouse using `ClickHouseBulkStep`.

### 6. Cassandra Write (`cassandra_example.py`)
Demonstrates how to write data into Apache Cassandra clusters using `CassandraWriteStep`.

---
*Each example requires a running database instance to execute (except SQLite).*
