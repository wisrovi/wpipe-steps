from wsqlite import Wsqlite
from typing import Any, Dict, Optional
from wpipe_steps.core.base import BaseStep
import json
from datetime import datetime

class SQLiteAuditStep(BaseStep):
    """
    Step for saving audit logs into SQLite using wsqlite.
    """
    
    def __init__(
        self, 
        db_path: str = "audit.db",
        table_name: str = "audit_logs",
        data_keys: Optional[list] = None,
        response_key: str = "audit_status",
        name: Optional[str] = None,
        version: str = "v2.0"
    ):
        super().__init__(name, version)
        self.db_path = db_path
        self.table_name = table_name
        self.data_keys = data_keys
        self.response_key = response_key

    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            with Wsqlite(db_name=self.db_path) as db:
                # Prepare payload
                if self.data_keys:
                    payload = {k: data.get(k) for k in self.data_keys}
                else:
                    payload = {k: v for k, v in data.items() if isinstance(v, (str, int, float, bool, dict, list)) and k != self.response_key}

                # wsqlite specific usage: setting input/details or direct execution
                # For audit, we can use the 'details' field or a custom table
                db.details = {
                    "timestamp": datetime.now().isoformat(),
                    "step_name": self.name,
                    "payload": payload
                }
                
                data[self.response_key] = {
                    "success": True,
                    "db_path": self.db_path,
                    "audit_id": db.id
                }
            return data
        except Exception as e:
            data[self.response_key] = {"success": False, "error": str(e)}
            raise RuntimeError(f"Wsqlite Audit failed: {str(e)}")
