from typing import Any, Dict, Optional
from wpipe import to_obj
from wpipe_steps.core.base import BaseStep


class HFTextGenerationStep(BaseStep):
    def __init__(self, name=None, version="v1.0", model_name="gpt2", device="cpu", max_length=100, temperature=0.7, response_key="generated_text"):
        super().__init__(name, version)
        self.model_name = model_name
        self.device = device
        self.max_length = max_length
        self.temperature = temperature
        self.response_key = response_key
        self._pipeline = None

    @to_obj
    def _execute_impl(self, data: Dict[str, Any]) -> Dict[str, Any]:
        if self._pipeline is None:
            from transformers import pipeline
            self._pipeline = pipeline(task="text-generation", model=self.model_name, device=self.device, local_files_only=True)
        prompt = data.get("prompt", "")
        if not prompt:
            data[self.response_key] = {"error": "No prompt"}
            return data
        result = self._pipeline(prompt, max_length=self.max_length, temperature=self.temperature)
        data[self.response_key] = {"prompt": prompt, "generated": result[0]["generated_text"]}
        return data

    def execute(self, data):
        """Execute the step - required by BaseStep."""
        return self._execute_impl(data)
