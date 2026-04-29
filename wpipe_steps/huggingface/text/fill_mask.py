from typing import Any, Dict, Optional
from wpipe import to_obj
from wpipe_steps.core.base import BaseStep


class HFFillMaskStep(BaseStep):
    def __init__(self, name=None, version="v1.0", model_name="bert-base-uncased", device="cpu", top_k=5, response_key="fill_mask"):
        super().__init__(name, version)
        self.model_name = model_name
        self.device = device
        self.top_k = top_k
        self.response_key = response_key
        self._pipeline = None

    @to_obj
    def _execute_impl(self, data: Dict[str, Any]) -> Dict[str, Any]:
        if self._pipeline is None:
            from transformers import pipeline
            self._pipeline = pipeline(task="fill-mask", model=self.model_name, device=self.device, local_files_only=True)
        text = data.get("text", "")
        if not text:
            data[self.response_key] = {"error": "No text"}
            return data
        results = self._pipeline(text, top_k=self.top_k)
        data[self.response_key] = {"text": text, "predictions": results}
        return data

    def execute(self, data):
        """Execute the step - required by BaseStep."""
        return self._execute_impl(data)
