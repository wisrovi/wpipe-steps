from typing import Any, Dict, List, Optional
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep

@step
class HealthCheckStep(BaseStep):
    """
    Step for checking health of HTTP services.
    """
    def __init__(self, urls: List[str], name: Optional[str] = None, version: str = "v1.0", response_key: str = "health_status"):
        super().__init__(name, version)
        self.urls = urls
        self.response_key = response_key

    @to_obj
    def __call__(self, data: Dict[str, Any]) -> Dict[str, Any]:
        requests = self.ensure_dependency("requests")
        
        status = {}
        all_healthy = True
        
        for url in self.urls:
            try:
                response = requests.get(url, timeout=5)
                is_ok = response.ok
                status[url] = {"up": is_ok, "status_code": response.status_code}
                if not is_ok:
                    all_healthy = False
            except Exception as e:
                status[url] = {"up": False, "error": str(e)}
                all_healthy = False
                
        data[self.response_key] = {
            "all_healthy": all_healthy,
            "services": status
        }
        
        return data
