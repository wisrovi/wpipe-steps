"""Sentiment analysis step using HuggingFace transformers."""
from typing import Any, Dict, Optional
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep


@step
class HFSentimentAnalysisStep(BaseStep):
    """Analyze sentiment of text (positive/negative) using local models.

    Args:
        model_name: HuggingFace model for sentiment analysis.
        device: Device to run inference on (cpu/cuda).
        response_key: Key to store results in pipeline data.
    """

    def __init__(
        self,
        name: Optional[str] = None,
        version: str = "v1.0",
        model_name: str = "distilbert-base-uncased-finetuned-sst-2-english",
        device: str = "cpu",
        response_key: str = "sentiment",
    ):
        super().__init__(name, version)
        self.model_name = model_name
        self.device = device
        self.response_key = response_key
        self._pipeline = None

    @to_obj
    def __call__(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Run sentiment analysis on data['text']."""
        if self._pipeline is None:
            from transformers import pipeline

            self._pipeline = pipeline(
                task="sentiment-analysis",
                model=self.model_name,
                device=self.device,
                local_files_only=True,
            )

        text = data.get("text", "")
        if not text:
            data[self.response_key] = {"error": "No text provided"}
            return data

        results = self._pipeline(text)
        data[self.response_key] = {"text": text, "sentiment": results[0]}
        return data
