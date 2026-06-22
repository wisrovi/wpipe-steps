from typing import Any, Dict, Optional
from wpipe_steps.core.base import BaseStep


class HFImageColorizationStep(BaseStep):
    def __init__(self, name=None, version="v1.0", model_name="paints-uchar/DeOldify", device="cpu", response_key="colorized"):
        super().__init__(name, version)
        self.model_name = model_name
        self.device = device
        self.response_key = response_key
    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        if pipe is None:
            from transformers import pipeline
            pipe = pipeline(task="image-to-image", model=self.model_name, device=self.device, local_files_only=True)
        image = data.get("image", "")
        if not image:
            data[self.response_key] = {"error": "image required"}
            return data
        result = pipe(image)
        data[self.response_key] = {"output_shape": list(result.shape), "colorized": True}
        return data
