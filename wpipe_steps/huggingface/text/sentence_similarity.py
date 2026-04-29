"""Sentence similarity step using HuggingFace transformers."""
from typing import Any, Dict, Optional
from wpipe_steps.core.base import BaseStep

class HFSentenceSimilarityStep(BaseStep):
    """Calculate similarity between sentences using local HuggingFace models.

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
        self._pipeline = None

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
        text1 = data.get("text1", "")
        text2 = data.get("text2", "")
        if not text1 or not text2:
            return data
        
        pipe = self._get_pipeline()
        import numpy as np
        
        vec1 = np.mean(pipe(text1)[0], axis=0)
        vec2 = np.mean(pipe(text2)[0], axis=0)
        
        similarity = float(np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2)))
        
        response_key = self.response_key or "similarity_score"
        data[response_key] = similarity
        return data
