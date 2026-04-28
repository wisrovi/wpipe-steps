# 🌐 Connectivity Examples

This directory contains examples of how to use connectivity-related steps in your pipelines.

## Examples included:

### 1. HTTP Request (`http_example.py`)
Shows how to perform standard REST API calls (GET, POST, etc.) using `HttpRequestStep`.

### 2. GraphQL Query (`graphql_example.py`)
Demonstrates how to execute GraphQL queries with variables and headers using `GraphQLQueryStep`.

### 3. Webhook Trigger (`webhook_example.py`)
Demonstrates how to trigger external webhooks with custom payloads using `WebhookTriggerStep`.

### 4. SFTP Transfer (`sftp_example.py`)
Demonstrates how to upload and download files securely using `SftpTransferStep` (Requires `paramiko`).

### 5. RSS Parser (`rss_example.py`)
Demonstrates how to parse RSS/Atom feeds to extract latest entries using `RSSParserStep` (Requires `feedparser`).

### 6. OAuth2 Authentication (`oauth2_example.py`)
Demonstrates how to retrieve access tokens using the Client Credentials flow with `OAuth2AuthStep`.

---
*Each example can be run directly from the terminal.*
