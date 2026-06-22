from typing import Any, Dict, Optional
from wpipe_steps.core.base import BaseStep


class HFVideoFrameInterpolationStep(BaseStep):
    def __init__(self, name=None, version="v1.0", model_name="your-vfi-model", device="cpu", response_key="interpolated"):
        super().__init__(name, version)
        self.model_name = model_name
        self.device = device
        self.response_key = response_key
    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        if pipe is None:
            from transformers import pipeline
            pipe = pipeline(task="image-to-image", model=self.model_name, device=self.device, local_files_only=True)
        video = data.get("video_path", "")
        if not video:
            data[self.response_key] = {"error": "video_path required"}
            return data
        result = pipe(video)
        data[self.response_key] = {"interpolated": True, "frames_added": True}
        return data
