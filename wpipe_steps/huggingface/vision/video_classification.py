from typing import Any, Dict, Optional
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep


@step
class HFVideoClassificationStep(BaseStep):
    def __init__(self, name=None, version="v1.0", model_name="MCG-NJU/VATEX-little-vivit", device="cpu", response_key="video_class"):
        super().__init__(name, version)
        self.model_name = model_name
        self.device = device
        self.response_key = response_key
        self._pipeline = None

    @to_obj
    def __call__(self, data: Dict[str, Any]) -> Dict[str, Any]:
        if self._pipeline is None:
            from transformers import pipeline
            self._pipeline = pipeline(task="video-classification", model=self.model_name, device=self.device, local_files_only=True)
        video = data.get("video_path", "")
        if not video:
            data[self.response_key] = {"error": "video_path required"}
            return data
        result = self._pipeline(video)
        data[self.response_key] = {"video": video, "predictions": result[:5]}
        return data
