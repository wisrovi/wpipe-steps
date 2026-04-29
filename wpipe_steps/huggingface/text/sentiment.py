"""Sentiment analysis step using HuggingFace transformers."""
from typing import Any, Dict, Optional
from wpipe_steps.core.base import BaseStep


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

    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Execute the step - required by BaseStep."""
        # Handle both dict and SimpleNamespace
        if hasattr(data, 'text'):
            text = data.text
        elif isinstance(data, dict):
            text = data.get("text", "")
        else:
            text = ""

        if not text:
            result = {"error": "No text provided"}
            if isinstance(data, dict):
                data[self.response_key] = result
            else:
                setattr(data, self.response_key, result)
            return data

        # Lazy-load pipeline (avoid pickling issues)
        from transformers import pipeline
        try:
            # Try local files first
            pipe = pipeline(
                task="sentiment-analysis",
                model=self.model_name,
                device=self.device,
                local_files_only=True,
            )
        except Exception:
            # If not cached, download from HuggingFace
            print(f"Downloading model {self.model_name} (first time)...")
            pipe = pipeline(
                task="sentiment-analysis",
                model=self.model_name,
                device=self.device,
                local_files_only=False,
            )

        results = pipe(text)
        result = {"text": text, "sentiment": results[0]}

        if isinstance(data, dict):
            data[self.response_key] = result
        else:
            setattr(data, self.response_key, result)
        return data

        results = pipe(text)
        data[self.response_key] = {"text": text, "sentiment": results[0]}
        return data
