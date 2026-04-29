from typing import Any, Dict, Optional
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep


@step
class HFTextToSpeechStep(BaseStep):
    def __init__(self, name=None, version="v1.0", model_name="espnet/kan-bayashi_ljspeech_vits", device="cpu", response_key="tts_audio"):
        super().__init__(name, version)
        self.model_name = model_name
        self.device = device
        self.response_key = response_key
        self._pipeline = None

    @to_obj
    def __call__(self, data: Dict[str, Any]) -> Dict[str, Any]:
        if self._pipeline is None:
            from transformers import pipeline
            self._pipeline = pipeline(task="text-to-speech", model=self.model_name, device=self.device, local_files_only=True)
        text = data.get("text", "")
        if not text:
            data[self.response_key] = {"error": "text required"}
            return data
        result = self._pipeline(text)
        data[self.response_key] = {"text": text, "audio_length": len(result["audio"])}
        return data
