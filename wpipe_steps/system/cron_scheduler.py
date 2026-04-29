from typing import Any, Dict, Optional
from datetime import datetime
from wpipe_steps.core.base import BaseStep

class CronSchedulerStep(BaseStep):
    """
    Step for calculating next execution time based on a cron expression.
    """
    def __init__(self, cron_expr: str, name: Optional[str] = None, version: str = "v1.0", response_key: str = "cron_status"):
        super().__init__(name, version)
        self.cron_expr = cron_expr
        self.response_key = response_key

    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        croniter = self.ensure_dependency("croniter")
        
        now = datetime.now()
        cron = croniter.croniter(self.cron_expr, now)
        next_run = cron.get_next(datetime)
        
        data[self.response_key] = {
            "cron_expression": self.cron_expr,
            "current_time": now.isoformat(),
            "next_execution": next_run.isoformat()
        }
        
        return data
