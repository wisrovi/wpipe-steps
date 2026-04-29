from typing import Any, Dict, Optional
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep


@step
class HFSpeakerDiarizationStep(BaseStep):
    def __init__(self, name=None, version="v1.0", model_name="pyannote/speaker-diarization", device="cpu", response_key="diarization"):
        super().__init__(name, version)
        self.model_name = model_name
        self.device = device
        self.response_key = response_key
        self._pipeline = None

    @to_obj
    def __call__(self, data: Dict[str, Any]) -> Dict[str, Any]:
        if self._pipeline is None:
            from pyannote.audio import Pipeline
            self._pipeline = Pipeline.from_pretrained(self.model_name)
        audio = data.get("audio_path", "")
        if not audio:
            data[self.response_key] = {"error": "audio_path required"}
            return data
        result = self._pipeline(audio)
        data[self.response_key] = {"audio": audio, "speakers": len(result.labels)}
        return data
