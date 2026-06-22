from typing import Any, Dict, Optional
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep

@step(
    name="image_resizer",
    version="v1.0",
    description="Resize images for web optimization",
    tags=["multimedia", "image", "sync"]
)
class ImageResizerStep(BaseStep):
    """
    Step for resizing images.
    Requires 'Pillow' library.
    """
    
    def __init__(
        self,
        input_path: str,
        output_path: Optional[str] = None,
        width: int = 800,
        height: Optional[int] = None,
        response_key: str = "image_status",
        name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__(name, version)
        self.input_path = input_path
        self.output_path = output_path or input_path.replace(".", "_resized.")
        self.width = width
        self.height = height
        self.response_key = response_key

    @to_obj
    def __call__(self, data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            PIL = self.ensure_dependency("PIL", "Pillow")
            
            img = PIL.Image.open(self.input_path)
            
            if self.height is None:
                # Maintain aspect ratio
                ratio = self.width / img.width
                self.height = int(img.height * ratio)
            
            resized = img.resize((self.width, self.height), PIL.Image.Resampling.LANCZOS)
            resized.save(self.output_path)
            
            data[self.response_key] = {
                "success": True,
                "input": self.input_path,
                "output": self.output_path,
                "size": f"{self.width}x{self.height}"
            }
            return data
            
        except Exception as e:
            data[self.response_key] = {"success": False, "error": str(e)}
            raise RuntimeError(f"Image Resizer failed: {str(e)}")
