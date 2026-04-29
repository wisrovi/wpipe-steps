from typing import Any, Dict, Optional
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep


@step
class HFMultipleChoiceStep(BaseStep):
    def __init__(self, name=None, version="v1.0", model_name="roberta-base", device="cpu", response_key="multiple_choice"):
        super().__init__(name, version)
        self.model_name = model_name
        self.device = device
        self.response_key = response_key
        self._pipeline = None

    @to_obj
    def __call__(self, data: Dict[str, Any]) -> Dict[str, Any]:
        if self._pipeline is None:
            from transformers import pipeline
            self._pipeline = pipeline(task="multiple-choice", model=self.model_name, device=self.device, local_files_only=True)
        context = data.get("context", "")
        question = data.get("question", "")
        choices = data.get("choices", [])
        if not all([context, question, choices]):
            data[self.response_key] = {"error": "context, question, choices required"}
            return data
        result = self._pipeline(context=context, question=question, choices=choices)
        data[self.response_key] = {"result": result}
        return data
