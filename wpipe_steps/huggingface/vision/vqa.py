from typing import Any, Dict, Optional
from wpipe import to_obj
from wpipe_steps.core.base import BaseStep


class HFVisualQuestionAnsweringStep(BaseStep):
    def __init__(self, name=None, version="v1.0", model_name="dandelin/vilt-b32-finetuned-vqa", device="cpu", response_key="vqa"):
        super().__init__(name, version)
        self.model_name = model_name
        self.device = device
        self.response_key = response_key
        self._pipeline = None

    @to_obj
    def _execute_impl(self, data: Dict[str, Any]) -> Dict[str, Any]:
        if self._pipeline is None:
            from transformers import pipeline
            self._pipeline = pipeline(task="visual-question-answering", model=self.model_name, device=self.device, local_files_only=True)
        image = data.get("image", "")
        question = data.get("question", "")
        if not image or not question:
            data[self.response_key] = {"error": "image and question required"}
            return data
        result = self._pipeline(image=image, question=question)
        data[self.response_key] = {"question": question, "answer": result}
        return data

    def execute(self, data):
        """Execute the step - required by BaseStep."""
        return self._execute_impl(data)
