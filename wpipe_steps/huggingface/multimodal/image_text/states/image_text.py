from typing import Any, Dict, Optional
from wpipe_steps.core.base import BaseStep


class HFImageTextToTextStep(BaseStep):
    """Multimodal models (BLIP2, LLaVA) for image+text to text."""
    def __init__(self, name=None, version="v1.0", model_name="Salesforce/blip2-flan-t5-xl", device="cpu", response_key="image_text"):
        super().__init__(name, version)
        self.model_name = model_name
        self.device = device
        self.response_key = response_key
    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        if pipe is None:
            from transformers import pipeline
            pipe = pipeline(task="image-to-text", model=self.model_name, device=self.device, local_files_only=True)
        image = data.get("image", "")
        prompt = data.get("prompt", "")
        if not image:
            data[self.response_key] = {"error": "image required"}
            return data
        result = pipe(image, prompt=prompt)
        data[self.response_key] = {"prompt": prompt, "generated": result[0]["generated_text"]}
        return data
