from typing import Any, Dict, Optional
from wpipe_steps.core.base import BaseStep


class HFImageClassificationStep(BaseStep):
    """Classify images using local HuggingFace models."""

    def __init__(
        self,
        name: Optional[str] = None,
        version: str = "v1.0",
        model_name: str = "google/vit-base-patch16-224",
        device: str = "cpu",
        top_k: int = 5,
        response_key: str = "img_class",
    ):
        super().__init__(name, version)
        self.model_name = model_name
        self.device = device
        self.top_k = top_k
        self.response_key = response_key

    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Execute the step - required by BaseStep."""
        # Handle both dict and SimpleNamespace
        if hasattr(data, 'image_path'):
            image = data.image_path
        elif isinstance(data, dict):
            image = data.get("image_path", "")
        else:
            image = ""

        if not image:
            result = {"error": "image_path required"}
            if isinstance(data, dict):
                data[self.response_key] = result
            else:
                setattr(data, self.response_key, result)
            return data

        # Lazy-load pipeline (avoid pickling issues)
        from transformers import pipeline
        try:
            # Try local files first
            pipe = pipeline(
                task="image-classification",
                model=self.model_name,
                device=self.device,
            )
        except Exception:
            # If not cached, download from HuggingFace
            print(f"Downloading model {self.model_name} (first time)...")
            pipe = pipeline(
                task="image-classification",
                model=self.model_name,
                device=self.device,
            )

        result = pipe(image)
        output = {"image": image, "predictions": result[:self.top_k]}

        if isinstance(data, dict):
            data[self.response_key] = output
        else:
            setattr(data, self.response_key, output)
        return data
