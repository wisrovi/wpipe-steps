# 🧱 HFRerankingStep

Rerank documents based on relevance to a query using local HuggingFace models.

## 📂 Structure
This step follows the WPipe professional package structure:
- `config/`: Configuration constants.
- `examples/`: Code examples.
- `exceptions/`: Custom step exceptions.
- `schemas/`: Pydantic input/output schemas.
- `states/`: Actual step execution logic.
- `utils/`: Internal helper utilities.
- `wrappers/`: Third-party library wrappers.

## ⚙️ Configuration
Namespace: `wpipe_steps.huggingface.text.reranking`

## 🚀 How to Use
```python
from wpipe_steps.huggingface.text.reranking import HFRerankingStep
```
