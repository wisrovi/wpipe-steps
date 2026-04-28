from wclickhouse import Wclickhouse
from typing import Any, Dict, Optional, List
from wpipe_steps.core.base import BaseStep

class ClickHouseBulkStep(BaseStep):
    """
    Step for bulk inserting data into ClickHouse using wclickhouse.
    """
    
    def __init__(
        self, 
        host: str,
        database: str,
        table: str,
        user: str = "default",
        password: str = "",
        port: int = 8123,
        data_key: Optional[str] = None, # Key in 'data' to get list of dicts/tuples
        custom_data: Optional[List[Any]] = None,
        response_key: str = "clickhouse_status",
        name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__(name, version)
        self.config = {
            "host": host,
            "database": database,
            "user": user,
            "password": password,
            "port": port
        }
        self.table = table
        self.data_key = data_key
        self.custom_data = custom_data
        self.response_key = response_key

    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            with Wclickhouse(**self.config) as ch:
                # Determine data to insert
                records = data.get(self.data_key) if self.data_key else self.custom_data
                if records is None:
                    raise ValueError("No data provided for ClickHouse bulk insert")

                # Assuming wclickhouse has a bulk_insert or similar method
                # We'll use the most common interface for your libraries
                ch.insert(self.table, records)
                
                data[self.response_key] = {
                    "success": True,
                    "table": self.table,
                    "count": len(records)
                }
            return data
        except Exception as e:
            data[self.response_key] = {"success": False, "error": str(e)}
            raise RuntimeError(f"Wclickhouse Bulk Insert failed: {str(e)}")
