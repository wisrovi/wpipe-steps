"""Document reranking step using HuggingFace transformers."""
from typing import Any, Dict, Optional
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep

@step
class HFRerankingStep(BaseStep):
    """Rerank documents based on relevance to a query using local HuggingFace models.

    Args:
        model_name: HuggingFace model for reranking.
        response_key: Key to store results in pipeline data.
    """

    def __init__(
        self,
        name: Optional[str] = None,
        model_name: str = "cross-encoder/ms-marco-MiniLM-L-6-v2",
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
                "text-classification",
                model=self.model_name,
                local_files_only=True
            )
        return self._pipeline

    @to_obj
    def __call__(self, data: Dict[str, Any]) -> Dict[str, Any]:
        query = data.get("query", "")
        documents = data.get("documents", [])
        if not query or not documents:
            return data
        
        pipe = self._get_pipeline()
        scores = []
        for doc in documents:
            result = pipe(f"{query} [SEP] {doc}")
            scores.append((doc, result[0]["score"]))
        
        scores.sort(key=lambda x: x[1], reverse=True)
        response_key = self.response_key or "ranked_docs"
        data[response_key] = [doc for doc, score in scores]
        return data
