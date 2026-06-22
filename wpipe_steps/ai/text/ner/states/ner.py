from typing import Any, Dict, Optional
from wpipe_steps.core.base import BaseStep


class HFNerStep(BaseStep):
    def __init__(self, name=None, version="v1.0", model_name="dbmdz/bert-large-cased-finetuned-conll03-english", device="cpu", aggregation_strategy="simple", response_key="ner_entities"):
        super().__init__(name, version)
        self.model_name = model_name
        self.device = device
        self.aggregation_strategy = aggregation_strategy
        self.response_key = response_key
    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        if pipe is None:
            from transformers import pipeline
            pipe = pipeline(task="ner", model=self.model_name, device=self.device, local_files_only=True, aggregation_strategy=self.aggregation_strategy)
        text = data.get("text", "")
        if not text:
            data[self.response_key] = {"error": "No text"}
            return data
        entities = pipe(text)
        data[self.response_key] = {"text": text, "entities": entities}
        return data
