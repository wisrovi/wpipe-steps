"""Text classification step using HuggingFace transformers."""
from typing import Any, Dict, Optional
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep


@step
class HFTextClassificationStep(BaseStep):
    """Classify text into predefined categories using local HuggingFace models.

    Args:
        model_name: HuggingFace model for text classification.
        device: Device to run inference on (cpu/cuda).
        top_k: Number of top results to return.
        response_key: Key to store results in pipeline data.
    """

    def __init__(
        self,
        name: Optional[str] = None,
        version: str = "v1.0",
        model_name: str = "distilbert-base-uncased-finetuned-sst-2-english",
        device: str = "cpu",
        top_k: int = 1,
        response_key: str = "text_classification",
    ):
        super().__init__(name, version)
        self.model_name = model_name
        self.device = device
        self.top_k = top_k
        self.response_key = response_key
        self._pipeline = None

    @to_obj
    def __call__(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Run text classification on data['text']."""
        if self._pipeline is None:
            from transformers import pipeline

            self._pipeline = pipeline(
                task="text-classification",
                model=self.model_name,
                device=self.device,
                local_files_only=True,
            )

        text = data.get("text", "")
        if not text:
            data[self.response_key] = {"error": "No text provided"}
            return data

        results = self._pipeline(text, top_k=self.top_k)
        data[self.response_key] = {"text": text, "predictions": results}
        return data
