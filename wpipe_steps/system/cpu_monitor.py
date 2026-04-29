from typing import Any, Dict, Optional
from wpipe_steps.core.base import BaseStep

class CpuMonitorStep(BaseStep):
    """
    Step for monitoring CPU usage.
    """
    def __init__(self, name: Optional[str] = None, version: str = "v1.0", threshold_percent: float = 90.0, response_key: str = "cpu_status"):
        super().__init__(name, version)
        self.threshold_percent = threshold_percent
        self.response_key = response_key

    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        psutil = self.ensure_dependency("psutil")
        
        cpu_percent = psutil.cpu_percent(interval=1)
        is_overloaded = cpu_percent >= self.threshold_percent
        
        data[self.response_key] = {
            "cpu_percent": cpu_percent,
            "is_overloaded": is_overloaded,
            "threshold": self.threshold_percent
        }
        
        return data
