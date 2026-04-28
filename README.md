# 🧱 WPipe Steps

**A professional collection of pre-built, production-ready steps and states for the WPipe orchestration engine.**

WPipe Steps provides a comprehensive library of modular components ("Steps") that can be easily integrated into your WPipe pipelines. Instead of reinventing the wheel for common tasks like API calls, database queries, or notifications, simply import and use a pre-built step.

---

## 📂 Professional Structure

The library is organized into logical "Packs" based on functionality:

| Pack | Namespace | Description |
|------|-----------|-------------|
| 🌐 **Connectivity** | `wpipe_steps.connectivity` | **HttpRequestStep**: REST/APIs client. <br> **GraphQLQueryStep**: GraphQL executor. <br> **WebhookTriggerStep**: Webhook notifier. <br> **SftpTransferStep**: SFTP transfer. <br> **RSSParserStep**: RSS/Atom feed parser. |
| 📊 **Database** | `wpipe_steps.database` | MySQL, Redis, MongoDB, ClickHouse, SQLite. |
| 🛡️ **Security** | `wpipe_steps.security` | Nmap, Shodan, Vault, Inyection Filtering. |
| ☁️ **Infrastructure** | `wpipe_steps.infrastructure` | AWS S3, Docker, Kubernetes, Terraform. |
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
