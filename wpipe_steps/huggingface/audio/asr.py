from typing import Any, Dict, Optional
from wpipe import to_obj
from wpipe_steps.core.base import BaseStep


class HFAutomaticSpeechRecognitionStep(BaseStep):
    """Transcribe audio to text using Whisper."""
    def __init__(self, name=None, version="v1.0", model_name="openai/whisper-tiny", device="cpu", response_key="transcription"):
        super().__init__(name, version)
        self.model_name = model_name
        self.device = device
        self.response_key = response_key
        self._pipeline = None

    @to_obj
    def _execute_impl(self, data: Dict[str, Any]) -> Dict[str, Any]:
        if self._pipeline is None:
            from transformers import pipeline
            self._pipeline = pipeline(task="automatic-speech-recognition", model=self.model_name, device=self.device, local_files_only=True)
        audio = data.get("audio_path", "")
        if not audio:
            data[self.response_key] = {"error": "audio_path required"}
            return data
        result = self._pipeline(audio)
        data[self.response_key] = {"audio": audio, "text": result["text"]}
        return data

    def execute(self, data):
        """Execute the step - required by BaseStep."""
        return self._execute_impl(data)
