from typing import Any, Dict, Optional
from wpipe import to_obj
from wpipe_steps.core.base import BaseStep


class HFZeroShotClassificationStep(BaseStep):
    def __init__(self, candidate_labels, name=None, version="v1.0", model_name="facebook/bart-large-mnli", device="cpu", response_key="zero_shot"):
        super().__init__(name, version)
        self.candidate_labels = candidate_labels
        self.model_name = model_name
        self.device = device
        self.response_key = response_key
        self._pipeline = None

    @to_obj
    def _execute_impl(self, data: Dict[str, Any]) -> Dict[str, Any]:
        if self._pipeline is None:
            from transformers import pipeline
            self._pipeline = pipeline(task="zero-shot-classification", model=self.model_name, device=self.device, local_files_only=True)
        text = data.get("text", "")
        if not text:
            data[self.response_key] = {"error": "No text"}
            return data
        results = self._pipeline(text, candidate_labels=self.candidate_labels)
        data[self.response_key] = {"text": text, "results": results}
        return data

    def execute(self, data):
        """Execute the step - required by BaseStep."""
        return self._execute_impl(data)
