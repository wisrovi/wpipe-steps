"""Text classification step using HuggingFace transformers."""
from typing import Any, Dict, Optional
from wpipe_steps.core.base import BaseStep


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
                task="text-classification",
                model=self.model_name,
                device=self.device,
                local_files_only=True,
            )
        except Exception:
            # If not cached, download from HuggingFace
            print(f"Downloading model {self.model_name} (first time)...")
            pipe = pipeline(
                task="text-classification",
                model=self.model_name,
                device=self.device,
                local_files_only=False,
            )
        
        results = pipe(text, top_k=self.top_k)
        result = {"text": text, "predictions": results}
        
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
                task="text-classification",
                model=self.model_name,
                device=self.device,
                local_files_only=True,
            )
        except Exception:
            # If not cached, download from HuggingFace
            print(f"Downloading model {self.model_name} (first time)...")
            pipe = pipeline(
                task="text-classification",
                model=self.model_name,
                device=self.device,
                local_files_only=False,
            )
        
        results = pipe(text, top_k=self.top_k)
        result = {"text": text, "predictions": results}
        
        if isinstance(data, dict):
            data[self.response_key] = result
        else:
            setattr(data, self.response_key, result)
        return data

        pipeline = self._get_pipeline()
        results = pipeline(text, top_k=self.top_k)
        
        result = {"text": text, "predictions": results}
        if isinstance(data, dict):
            data[self.response_key] = result
        else:
            setattr(data, self.response_key, result)
        return data
