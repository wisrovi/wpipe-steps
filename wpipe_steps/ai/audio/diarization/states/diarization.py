from typing import Any, Dict, Optional
from wpipe_steps.core.base import BaseStep


class HFSpeakerDiarizationStep(BaseStep):
    def __init__(self, name=None, version="v1.0", model_name="pyannote/speaker-diarization", device="cpu", response_key="diarization"):
        super().__init__(name, version)
        self.model_name = model_name
        self.device = device
        self.response_key = response_key
    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        if pipe is None:
            from pyannote.audio import Pipeline
            pipe = Pipeline.from_pretrained(self.model_name)
        audio = data.get("audio_path", "")
        if not audio:
            data[self.response_key] = {"error": "audio_path required"}
            return data
        result = pipe(audio)
        data[self.response_key] = {"audio": audio, "speakers": len(result.labels)}
        return data
