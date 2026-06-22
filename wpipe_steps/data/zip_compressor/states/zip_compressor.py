from typing import Any, Dict, Optional, List
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep

@step(
    name="zip_compressor",
    version="v1.0",
    description="Compress folders for logs or backups",
    tags=["data", "zip", "sync"]
)
class ZipCompressorStep(BaseStep):
    """
    Step for compressing folders/files into ZIP.
    """
    
    def __init__(
        self,
        input_path: str,
        output_path: Optional[str] = None,
        response_key: str = "zip_status",
        name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__(name, version)
        self.input_path = input_path
        self.output_path = output_path or input_path + ".zip"
        self.response_key = response_key

    @to_obj
    def __call__(self, data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            import zipfile
            import os
            
            with zipfile.ZipFile(self.output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                if os.path.isdir(self.input_path):
                    for root, dirs, files in os.walk(self.input_path):
                        for file in files:
                            file_path = os.path.join(root, file)
                            arcname = os.path.relpath(file_path, self.input_path)
                            zipf.write(file_path, arcname)
                else:
                    zipf.write(self.input_path, os.path.basename(self.input_path))
            
            data[self.response_key] = {
                "success": True,
                "input": self.input_path,
                "output": self.output_path
            }
            return data
            
        except Exception as e:
            data[self.response_key] = {"success": False, "error": str(e)}
            raise RuntimeError(f"Zip Compressor failed: {str(e)}")
