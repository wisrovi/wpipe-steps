from typing import Any, Dict, Optional
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep


@step
class HFImageToTextStep(BaseStep):
    """Generate text description of image."""
    def __init__(self, name=None, version="v1.0", model_name="Salesforce/blip-image-captioning-base", device="cpu", response_key="caption"):
        super().__init__(name, version)
        self.model_name = model_name
        self.device = device
        self.response_key = response_key
        self._pipeline = None

    @to_obj
    def __call__(self, data: Dict[str, Any]) -> Dict[str, Any]:
        if self._pipeline is None:
            from transformers import pipeline
            self._pipeline = pipeline(task="image-to-text", model=self.model_name, device=self.device, local_files_only=True)
        image = data.get("image", "")
        if not image:
            data[self.response_key] = {"error": "image required"}
            return data
        result = self._pipeline(image)
        data[self.response_key] = {"image": image, "caption": result[0]["generated_text"]}
        return data
