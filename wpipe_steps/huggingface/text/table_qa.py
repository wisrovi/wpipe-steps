from typing import Any, Dict, Optional
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep


@step
class HFTableQuestionAnsweringStep(BaseStep):
    def __init__(self, name=None, version="v1.0", model_name="google/tapas-base", device="cpu", response_key="table_qa"):
        super().__init__(name, version)
        self.model_name = model_name
        self.device = device
        self.response_key = response_key
        self._pipeline = None

    @to_obj
    def __call__(self, data: Dict[str, Any]) -> Dict[str, Any]:
        if self._pipeline is None:
            from transformers import pipeline
            self._pipeline = pipeline(task="table-question-answering", model=self.model_name, device=self.device, local_files_only=True)
        table = data.get("table")
        query = data.get("query", "")
        if not table or not query:
            data[self.response_key] = {"error": "table and query required"}
            return data
        result = self._pipeline(table=table, query=query)
        data[self.response_key] = {"result": result}
        return data
