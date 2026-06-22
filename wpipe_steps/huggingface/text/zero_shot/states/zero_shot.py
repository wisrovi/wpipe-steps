from typing import Any, Dict, Optional
from wpipe_steps.core.base import BaseStep


class HFZeroShotClassificationStep(BaseStep):
    def __init__(self, candidate_labels, name=None, version="v1.0", model_name="facebook/bart-large-mnli", device="cpu", response_key="zero_shot"):
        super().__init__(name, version)
        self.candidate_labels = candidate_labels
        self.model_name = model_name
        self.device = device
        self.response_key = response_key
    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        if pipe is None:
            from transformers import pipeline
            pipe = pipeline(task="zero-shot-classification", model=self.model_name, device=self.device, local_files_only=True)
        text = data.get("text", "")
        if not text:
            data[self.response_key] = {"error": "No text"}
            return data
        results = pipe(text, candidate_labels=self.candidate_labels)
        data[self.response_key] = {"text": text, "results": results}
        return data
