# 🧱 HFAutomaticSpeechRecognitionStep

Transcribe audio to text using Whisper.

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
Namespace: `wpipe_steps.huggingface.audio.asr`

## 🚀 How to Use
```python
from wpipe_steps.huggingface.audio.asr import HFAutomaticSpeechRecognitionStep
```
