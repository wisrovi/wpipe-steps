"""Semantic search step using HuggingFace transformers."""
from typing import Any, Dict, Optional
from wpipe_steps.core.base import BaseStep

class HFSemanticSearchStep(BaseStep):
    """Perform semantic search over documents using local HuggingFace models.

    Args:
        model_name: HuggingFace model for sentence embeddings.
        top_k: Number of top results to return.
        response_key: Key to store results in pipeline data.
    """

    def __init__(
        self,
        name: Optional[str] = None,
        model_name: str = "sentence-transformers/all-MiniLM-L6-v2",
        top_k: int = 5,
        response_key: Optional[str] = None,
        **kwargs
    ):
        super().__init__(name=name, **kwargs)
        self.model_name = model_name
        self.top_k = top_k
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
        query = data.get("query", "")
        documents = data.get("documents", [])
        if not query or not documents:
            return data
        
        pipe = self._get_pipeline()
        import numpy as np
        
        query_emb = np.mean(pipe(query)[0], axis=0)
        results = []
        for doc in documents:
            doc_emb = np.mean(pipe(doc)[0], axis=0)
            score = float(np.dot(query_emb, doc_emb) / (np.linalg.norm(query_emb) * np.linalg.norm(doc_emb)))
            results.append((doc, score))
        
        results.sort(key=lambda x: x[1], reverse=True)
        top_results = results[:self.top_k]
        
        response_key = self.response_key or "search_results"
        data[response_key] = [{"document": doc, "score": score} for doc, score in top_results]
        return data
