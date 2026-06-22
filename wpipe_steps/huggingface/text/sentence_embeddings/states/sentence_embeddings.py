"""Sentence embeddings step using HuggingFace transformers."""
from typing import Any, Dict, Optional
from wpipe_steps.core.base import BaseStep

class HFSentenceEmbeddingsStep(BaseStep):
    """Generate sentence embeddings using local HuggingFace models.

    Args:
        model_name: HuggingFace model for sentence embeddings.
        response_key: Key to store results in pipeline data.
    """

    def __init__(
        self,
        name: Optional[str] = None,
        model_name: str = "sentence-transformers/all-MiniLM-L6-v2",
        response_key: Optional[str] = None,
        **kwargs
    ):
        super().__init__(name=name, **kwargs)
        self.model_name = model_name
        self.response_key = response_key
    def _get_pipeline(self):
        if self._pipeline is None:
            from transformers import pipeline
            self._pipeline = pipeline(
                "feature-extraction",
                model=self.model_name,
                local_files_only=True
            )
        return self._pipeline
    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        text = data.get("text", "")
        if not text:
            return data
        
        pipe = self._get_pipeline()
        import numpy as np
        embeddings = np.mean(pipe(text)[0], axis=0).tolist()
        
        response_key = self.response_key or "embeddings"
        data[response_key] = embeddings
        return data
