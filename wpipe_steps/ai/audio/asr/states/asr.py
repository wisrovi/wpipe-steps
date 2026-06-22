from typing import Any, Dict, Optional
from wpipe_steps.core.base import BaseStep


class HFAutomaticSpeechRecognitionStep(BaseStep):
    """Transcribe audio to text using Whisper."""

    def __init__(
        self,
        name: Optional[str] = None,
        version: str = "v1.0",
        model_name: str = "openai/whisper-tiny",
        device: str = "cpu",
        response_key: str = "transcription",
    ):
        super().__init__(name, version)
        self.model_name = model_name
        self.device = device
        self.response_key = response_key

    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Execute the step - required by BaseStep."""
        # Handle both dict and SimpleNamespace
        if hasattr(data, 'audio_path'):
            audio = data.audio_path
        elif isinstance(data, dict):
            audio = data.get("audio_path", "")
        else:
            audio = ""

        if not audio:
            result = {"error": "audio_path required"}
            if isinstance(data, dict):
                data[self.response_key] = result
            else:
                setattr(data, self.response_key, result)
            return data

        # Lazy-load pipeline (avoid pickling issues)
        from transformers import pipeline
        try:
            # Try local files first
            pipe = pipeline(
                task="automatic-speech-recognition",
                model=self.model_name,
                device=self.device,
                local_files_only=True,
            )
        except Exception:
            # If not cached, download from HuggingFace
            print(f"Downloading model {self.model_name} (first time)...")
            pipe = pipeline(
                task="automatic-speech-recognition",
                model=self.model_name,
                device=self.device,
                local_files_only=False,
            )

        result = pipe(audio)
        output = {"audio": audio, "text": result["text"]}

        if isinstance(data, dict):
            data[self.response_key] = output
        else:
            setattr(data, self.response_key, output)
        return data
