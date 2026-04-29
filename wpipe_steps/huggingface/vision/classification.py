from typing import Any, Dict, Optional
from wpipe_steps.core.base import BaseStep


class HFImageClassificationStep(BaseStep):
    def __init__(self, name=None, version="v1.0", model_name="google/vit-base-patch16-224", device="cpu", response_key="img_class"):
        super().__init__(name, version)
        self.model_name = model_name
        self.device = device
        self.response_key = response_key
        self._pipeline = None
    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        if self._pipeline is None:
            from transformers import pipeline
            self._pipeline = pipeline(task="image-classification", model=self.model_name, device=self.device, local_files_only=True)
        image = data.get("image", "")
        if not image:
            data[self.response_key] = {"error": "image required"}
            return data
        result = self._pipeline(image)
        data[self.response_key] = {"image": image, "predictions": result[:5]}
        return data
