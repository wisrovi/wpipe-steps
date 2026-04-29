"""Document question answering step using HuggingFace transformers."""
from typing import Any, Dict, Optional
from wpipe_steps.core.base import BaseStep

class HFDocumentQuestionAnsweringStep(BaseStep):
    """Answer questions from document images using local HuggingFace models.

    Args:
        model_name: HuggingFace model for document QA.
        response_key: Key to store results in pipeline data.
    """

    def __init__(
        self,
        name: Optional[str] = None,
        model_name: str = "impira/layoutlm-document-qa",
        response_key: Optional[str] = None,
        **kwargs
    ):
        super().__init__(name=name, **kwargs)
        self.model_name = model_name
        self.response_key = response_key
        self._pipeline = None

    def _get_pipeline(self):
        if self._pipeline is None:
            from transformers import pipeline
            self._pipeline = pipeline(
                "document-question-answering",
                model=self.model_name,
                local_files_only=True
            )
        return self._pipeline
    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        image = data.get("image", "")
        question = data.get("question", "")
        if not image or not question:
            return data
        
        pipe = self._get_pipeline()
        result = pipe(image=image, question=question)
        
        response_key = self.response_key or "doc_answer"
        data[response_key] = result
        return data
