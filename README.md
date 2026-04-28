# 🧱 WPipe Steps

**A professional collection of pre-built, production-ready steps and states for the WPipe orchestration engine.**

WPipe Steps provides a comprehensive library of modular components ("Steps") that can be easily integrated into your WPipe pipelines. Instead of reinventing the wheel for common tasks like API calls, database queries, or notifications, simply import and use a pre-built step.

---

## 📂 Professional Structure

The library is organized into logical "Packs" based on functionality:

| Pack | Namespace | Description |
|------|-----------|-------------|
| 🌐 **Connectivity** | `wpipe_steps.connectivity` | **HttpRequestStep**: REST client. <br> **GraphQLQueryStep**: GraphQL executor. <br> **WebhookTriggerStep**: Webhook notifier. <br> **SftpTransferStep**: SFTP transfer. <br> **RSSParserStep**: RSS parser. <br> **OAuth2AuthStep**: OAuth2 manager. |
| 📊 **Database** | `wpipe_steps.database` | **MySQLQueryStep**: MySQL SQL executor. <br> **Redis Steps**: Full Redis support via wredis (bitmaps, hash, sets, sorted sets, streams, pub/sub, queue, geo, hyperloglog, transactions, pipeline, cache decorators) - sync/async. <br> **MongoInsertStep**: MongoDB document inserter. <br> **SQLiteAuditStep**: Local SQLite audit logger. <br> **ClickHouseBulkStep**: ClickHouse massive data inserter. <br> **CassandraWriteStep**: Cassandra data writer. |
| 🛡️ **Security** | `wpipe_steps.security` | **Fail2BanCheckStep**: IP ban status verifier. <br> **NmapScanStep**: Port scanning discovery. <br> **ShodanSearchStep**: Network intelligence search. <br> **HashGeneratorStep**: Hash generator. <br> **VaultSecretsStep**: Vault secrets retriever. <br> **WafFilterStep**: SQLi/XSS input filter. |
| ☁️ **Infrastructure** | `wpipe_steps.infrastructure` | **S3BucketUploadStep**: AWS S3 file uploader. |
| 📧 **Communication** | `wpipe_steps.communication` | Telegram, Slack, Discord, SendGrid, Twilio. |
| 📁 **Data** | `wpipe_steps.data` | CSV, JSON, PDF, Excel, Image Processing. |
| 🎙️ **Multimedia** | `wpipe_steps.multimedia` | Audio Normalization, Whisper AI, TTS. |
| 🤖 **AI** | `wpipe_steps.ai` | OpenAI, HuggingFace, Sentiment Analysis. |
| ⚙️ **System** | `wpipe_steps.system` | Resource Monitoring, Shell Exec, Health Checks. |

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
