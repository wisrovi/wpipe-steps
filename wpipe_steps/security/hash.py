import hashlib
import os
from typing import Any, Dict, Optional, Literal
from wpipe_steps.core.base import BaseStep

class HashGeneratorStep(BaseStep):
    """
    Step for generating cryptographic hashes of strings or files.
    Supports MD5, SHA1, SHA256, SHA512.
    """
    
    def __init__(
        self, 
        algorithm: Literal["md5", "sha1", "sha256", "sha512"] = "sha256",
        input_key: Optional[str] = None, # Key in 'data' containing the string
        file_path: Optional[str] = None, # Path to the file to hash
        response_key: str = "hash_result",
        name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__(name, version)
        self.algorithm = algorithm.lower()
        self.input_key = input_key
        self.file_path = file_path
        self.response_key = response_key

    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        h = hashlib.new(self.algorithm)
        
        try:
            if self.file_path:
                if not os.path.exists(self.file_path):
                    raise FileNotFoundError(f"File not found: {self.file_path}")
                # Read file in chunks to avoid memory issues with large files
                with open(self.file_path, "rb") as f:
                    for chunk in iter(lambda: f.read(4096), b""):
                        h.update(chunk)
            elif self.input_key:
                val = str(data.get(self.input_key, ""))
                h.update(val.encode('utf-8'))
            else:
                raise ValueError("Either input_key or file_path must be provided")

            data[self.response_key] = {
                "success": True,
                "algorithm": self.algorithm,
                "hash": h.hexdigest()
            }
            return data
            
        except Exception as e:
            data[self.response_key] = {"success": False, "error": str(e)}
            raise RuntimeError(f"Hash Generation failed: {str(e)}")
