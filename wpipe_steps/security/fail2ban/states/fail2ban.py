import os
from typing import Any, Dict, Optional
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep

@step(
    name="fail2ban_check",
    version="v1.0",
    description="Check if IP is banned by Fail2Ban",
    tags=["security", "fail2ban", "sync"]
)
class Fail2BanCheckStep(BaseStep):
    """
    Step for checking if an IP is currently banned by Fail2Ban.
    Analyzes the fail2ban log file for 'Ban' events without 'Unban' counterparts.
    """

    def __init__(
        self,
        ip_to_check: str,
        log_path: str = "/var/log/fail2ban.log",
        response_key: str = "fail2ban_status",
        name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__(name, version)
        self.ip_to_check = ip_to_check
        self.log_path = log_path
        self.response_key = response_key

    @to_obj
    def __call__(self, data: Dict[str, Any]) -> Dict[str, Any]:
        if not os.path.exists(self.log_path):
            data[self.response_key] = {
                "success": False,
                "error": f"Log file not found at {self.log_path}",
                "is_banned": False
            }
            return data

        try:
            is_banned = False
            with open(self.log_path, 'r') as f:
                lines = f.readlines()
                for line in reversed(lines):
                    if self.ip_to_check in line:
                        if "Ban" in line:
                            is_banned = True
                            break
                        if "Unban" in line:
                            is_banned = False
                            break

            data[self.response_key] = {
                "success": True,
                "ip": self.ip_to_check,
                "is_banned": is_banned,
                "log_analyzed": self.log_path
            }
            return data

        except Exception as e:
            data[self.response_key] = {"success": False, "error": str(e)}
            raise RuntimeError(f"Fail2Ban Check failed: {str(e)}")
