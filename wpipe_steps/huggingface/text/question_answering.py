from typing import Any, Dict, Optional
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep


@step
class HFQuestionAnsweringStep(BaseStep):
    def __init__(self, name=None, version="v1.0", model_name="bert-large-uncased-whole-word-masking-finetuned-squad", device="cpu", response_key="qa_answer"):
        super().__init__(name, version)
        self.model_name = model_name
        self.device = device
        self.response_key = response_key
        self._pipeline = None

    @to_obj
    def __call__(self, data: Dict[str, Any]) -> Dict[str, Any]:
        if self._pipeline is None:
            from transformers import pipeline
            self._pipeline = pipeline(task="question-answering", model=self.model_name, device=self.device, local_files_only=True)
        context = data.get("context", "")
        question = data.get("question", "")
        if not context or not question:
            data[self.response_key] = {"error": "Context and question required"}
            return data
        result = self._pipeline(question=question, context=context)
        data[self.response_key] = {"question": question, "answer": result}
        return data
