from typing import Any, Dict, Optional
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep


@step
class HFImageStyleTransferStep(BaseStep):
    def __init__(self, name=None, version="v1.0", model_name="your-style-transfer-model", device="cpu", response_key="styled"):
        super().__init__(name, version)
        self.model_name = model_name
        self.device = device
        self.response_key = response_key
        self._pipeline = None

    @to_obj
    def __call__(self, data: Dict[str, Any]) -> Dict[str, Any]:
        if self._pipeline is None:
            from transformers import pipeline
            self._pipeline = pipeline(task="image-to-image", model=self.model_name, device=self.device, local_files_only=True)
        image = data.get("image", "")
        if not image:
            data[self.response_key] = {"error": "image required"}
            return data
        result = self._pipeline(image)
        data[self.response_key] = {"output_shape": list(result.shape), "styled": True}
        return data
