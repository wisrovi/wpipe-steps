from typing import Any, Dict, Optional
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep


@step
class HFDocumentVisualQuestionAnsweringStep(BaseStep):
    def __init__(self, name=None, version="v1.0", model_name="nielsr/layoutlmv3-finetuned-docvqa", device="cpu", response_key="doc_vqa"):
        super().__init__(name, version)
        self.model_name = model_name
        self.device = device
        self.response_key = response_key
        self._pipeline = None

    @to_obj
    def __call__(self, data: Dict[str, Any]) -> Dict[str, Any]:
        if self._pipeline is None:
            from transformers import pipeline
            self._pipeline = pipeline(task="document-question-answering", model=self.model_name, device=self.device, local_files_only=True)
        image = data.get("image", "")
        question = data.get("question", "")
        if not image or not question:
            data[self.response_key] = {"error": "image and question required"}
            return data
        result = self._pipeline(image=image, question=question)
        data[self.response_key] = {"question": question, "answer": result}
        return data
