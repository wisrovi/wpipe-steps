from typing import Any, Dict, Optional
import shutil
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep

@step
class DiskSpaceCheckStep(BaseStep):
    """
    Step for checking disk space.
    """
    def __init__(self, path: str = "/", name: Optional[str] = None, version: str = "v1.0", response_key: str = "disk_status", min_free_gb: float = 1.0):
        super().__init__(name, version)
        self.path = path
        self.response_key = response_key
        self.min_free_gb = min_free_gb

    @to_obj
    def __call__(self, data: Dict[str, Any]) -> Dict[str, Any]:
        total, used, free = shutil.disk_usage(self.path)
        free_gb = free / (2**30)
        
        data[self.response_key] = {
            "path": self.path,
            "total_gb": total / (2**30),
            "used_gb": used / (2**30),
            "free_gb": free_gb,
            "has_enough_space": free_gb >= self.min_free_gb
        }
        
        return data
