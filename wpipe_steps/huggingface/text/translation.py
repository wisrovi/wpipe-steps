from typing import Any, Dict, Optional
from wpipe_steps.core.base import BaseStep


class HFTranslationStep(BaseStep):
    def __init__(self, name=None, version="v1.0", model_name="t5-small", device="cpu", response_key="translation"):
        super().__init__(name, version)
        self.model_name = model_name
        self.device = device
        self.response_key = response_key
    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        if pipe is None:
            from transformers import pipeline
            pipe = pipeline(task="translation_en_to_fr", model=self.model_name, device=self.device, local_files_only=True)
        text = data.get("text", "")
        if not text:
            data[self.response_key] = {"error": "No text"}
            return data
        result = pipe(text)
        data[self.response_key] = {"original": text, "translated": result[0]["translation_text"]}
        return data
