from typing import Any, Dict, Optional
from wpipe import to_obj
from wpipe_steps.core.base import BaseStep


class HFVoiceActivityDetectionStep(BaseStep):
    def __init__(self, name=None, version="v1.0", model_name="speechbrain/vad-crdnn-libriparty", device="cpu", response_key="vad"):
        super().__init__(name, version)
        self.model_name = model_name
        self.device = device
        self.response_key = response_key
        self._model = None

    @to_obj
    def _execute_impl(self, data: Dict[str, Any]) -> Dict[str, Any]:
        if self._model is None:
            from speechbrain.pretrained import VAD
            self._model = VAD.from_hparams(self.model_name)
        audio = data.get("audio_path", "")
        if not audio:
            data[self.response_key] = {"error": "audio_path required"}
            return data
        result = self._model(audio)
        data[self.response_key] = {"audio": audio, "speech_detected": bool(result)}
        return data

    def execute(self, data):
        """Execute the step - required by BaseStep."""
        return self._execute_impl(data)
