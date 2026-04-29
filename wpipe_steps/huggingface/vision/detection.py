from typing import Any, Dict, Optional
from wpipe_steps.core.base import BaseStep


class HFObjectDetectionStep(BaseStep):
    def __init__(self, name=None, version="v1.0", model_name="facebook/detr-resnet-50", device="cpu", response_key="objects"):
        super().__init__(name, version)
        self.model_name = model_name
        self.device = device
        self.response_key = response_key
    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        if pipe is None:
            from transformers import pipeline
            pipe = pipeline(task="object-detection", model=self.model_name, device=self.device, local_files_only=True)
        image = data.get("image", "")
        if not image:
            data[self.response_key] = {"error": "image required"}
            return data
        result = pipe(image)
        data[self.response_key] = {"image": image, "objects": result}
        return data
