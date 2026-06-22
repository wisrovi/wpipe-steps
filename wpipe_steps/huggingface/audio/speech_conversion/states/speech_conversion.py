from typing import Any, Dict, Optional
from wpipe_steps.core.base import BaseStep


class HFSpeechToSpeechStep(BaseStep):
    def __init__(self, name=None, version="v1.0", model_name="your-model-here", device="cpu", response_key="converted_speech"):
        super().__init__(name, version)
        self.model_name = model_name
        self.device = device
        self.response_key = response_key
    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        if pipe is None:
            from transformers import pipeline
            pipe = pipeline(task="audio-to-audio", model=self.model_name, device=self.device, local_files_only=True)
        audio = data.get("audio_path", "")
        if not audio:
            data[self.response_key] = {"error": "audio_path required"}
            return data
        result = pipe(audio)
        data[self.response_key] = {"input": audio, "converted": True}
        return data
