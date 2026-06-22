from typing import Any, Dict, Optional
from wpipe_steps.core.base import BaseStep


class HFText2TextGenerationStep(BaseStep):
    def __init__(self, name=None, version="v1.0", model_name="t5-base", device="cpu", response_key="text2text"):
        super().__init__(name, version)
        self.model_name = model_name
        self.device = device
        self.response_key = response_key
    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        if pipe is None:
            from transformers import pipeline
            pipe = pipeline(task="text2text-generation", model=self.model_name, device=self.device, local_files_only=True)
        text = data.get("text", "")
        if not text:
            data[self.response_key] = {"error": "No text"}
            return data
        result = pipe(text)
        data[self.response_key] = {"input": text, "output": result[0]["generated_text"]}
        return data
