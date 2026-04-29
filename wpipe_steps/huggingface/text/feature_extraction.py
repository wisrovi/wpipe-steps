from typing import Any, Dict, Optional
from wpipe_steps.core.base import BaseStep


class HFFeatureExtractionStep(BaseStep):
    def __init__(self, name=None, version="v1.0", model_name="bert-base-uncased", device="cpu", response_key="features"):
        super().__init__(name, version)
        self.model_name = model_name
        self.device = device
        self.response_key = response_key
        self._pipeline = None
    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        if self._pipeline is None:
            from transformers import pipeline
            self._pipeline = pipeline(task="feature-extraction", model=self.model_name, device=self.device, local_files_only=True)
        text = data.get("text", "")
        if not text:
            data[self.response_key] = {"error": "No text"}
            return data
        result = self._pipeline(text)
        data[self.response_key] = {"text": text, "features_shape": [len(result), len(result[0]), len(result[0][0])]}
        return data
