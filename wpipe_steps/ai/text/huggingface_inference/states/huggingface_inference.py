from typing import Any, Dict, Optional
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep

@step(
    name="huggingface_inference",
    version="v1.0",
    description="Use open-source ML models",
    tags=["ai", "huggingface", "sync"]
)
class HuggingFaceInferenceStep(BaseStep):
    """
    Step for using HuggingFace Inference API.
    Requires 'huggingface-hub' library.
    """
    
    def __init__(
        self,
        api_key: str,
        model: str,
        inputs: Optional[Any] = None,
        inputs_key: Optional[str] = None,
        response_key: str = "hf_status",
        name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__(name, version)
        self.api_key = api_key
        self.model = model
        self.inputs = inputs
        self.inputs_key = inputs_key
        self.response_key = response_key

    @to_obj
    def __call__(self, data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            huggingface_hub = self.ensure_dependency("huggingface_hub")
            
            client = huggingface_hub.InferenceClient(token=self.api_key)
            
            inputs = self.inputs or data.get(self.inputs_key)
            
            result = client.text_generation(
                prompt=str(inputs),
                model=self.model,
                max_new_tokens=100
            )
            
            data[self.response_key] = {
                "success": True,
                "model": self.model,
                "result": result
            }
            return data
            
        except Exception as e:
            data[self.response_key] = {"success": False, "error": str(e)}
            raise RuntimeError(f"HuggingFace Inference failed: {str(e)}")
