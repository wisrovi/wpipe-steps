from typing import Any, Dict, Optional
from wpipe_steps.core.base import BaseStep


class HFSummarizationStep(BaseStep):
    def __init__(self, name=None, version="v1.0", model_name="facebook/bart-large-cnn", device="cpu", max_length=150, min_length=30, response_key="summary"):
        super().__init__(name, version)
        self.model_name = model_name
        self.device = device
        self.max_length = max_length
        self.min_length = min_length
        self.response_key = response_key
    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        if pipe is None:
            from transformers import pipeline
            pipe = pipeline(task="summarization", model=self.model_name, device=self.device, local_files_only=True)
        text = data.get("text", "")
        if not text:
            data[self.response_key] = {"error": "No text"}
            return data
        result = pipe(text, max_length=self.max_length, min_length=self.min_length)
        data[self.response_key] = {"original": text, "summary": result[0]["summary_text"]}
        return data
