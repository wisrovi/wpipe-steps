from typing import Any, Dict, Optional
from wpipe_steps.core.base import BaseStep


class HFAnyToAnyStep(BaseStep):
    """Any-to-any multimodal models."""
    def __init__(self, name=None, version="v1.0", model_name="your-any2any-model", device="cpu", response_key="any2any"):
        super().__init__(name, version)
        self.model_name = model_name
        self.device = device
        self.response_key = response_key
        self._pipeline = None
    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        if self._pipeline is None:
            from transformers import pipeline
            self._pipeline = pipeline(task="image-to-text", model=self.model_name, device=self.device, local_files_only=True)
        input_data = data.get("input", "")
        if not input_data:
            data[self.response_key] = {"error": "input required"}
            return data
        result = self._pipeline(input_data)
        data[self.response_key] = {"output": result}
        return data
