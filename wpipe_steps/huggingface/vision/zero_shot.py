from typing import Any, Dict, Optional
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep


@step
class HFZeroShotImageClassificationStep(BaseStep):
    def __init__(self, name=None, version="v1.0", model_name="openai/clip-vit-base-patch32", device="cpu", response_key="zero_shot_img"):
        super().__init__(name, version)
        self.model_name = model_name
        self.device = device
        self.response_key = response_key
        self._pipeline = None

    @to_obj
    def __call__(self, data: Dict[str, Any]) -> Dict[str, Any]:
        if self._pipeline is None:
            from transformers import pipeline
            self._pipeline = pipeline(task="zero-shot-image-classification", model=self.model_name, device=self.device, local_files_only=True)
        image = data.get("image", "")
        labels = data.get("labels", [])
        if not image or not labels:
            data[self.response_key] = {"error": "image and labels required"}
            return data
        result = self._pipeline(image, candidate_labels=labels)
        data[self.response_key] = {"image": image, "results": result}
        return data
