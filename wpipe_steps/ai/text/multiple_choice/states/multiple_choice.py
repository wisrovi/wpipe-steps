from typing import Any, Dict, Optional
from wpipe_steps.core.base import BaseStep


class HFMultipleChoiceStep(BaseStep):
    def __init__(self, name=None, version="v1.0", model_name="roberta-base", device="cpu", response_key="multiple_choice"):
        super().__init__(name, version)
        self.model_name = model_name
        self.device = device
        self.response_key = response_key
    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        if pipe is None:
            from transformers import pipeline
            pipe = pipeline(task="multiple-choice", model=self.model_name, device=self.device, local_files_only=True)
        context = data.get("context", "")
        question = data.get("question", "")
        choices = data.get("choices", [])
        if not all([context, question, choices]):
            data[self.response_key] = {"error": "context, question, choices required"}
            return data
        result = pipe(context=context, question=question, choices=choices)
        data[self.response_key] = {"result": result}
        return data
