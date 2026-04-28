from typing import Any, Dict, Optional, Union
from wpipe_steps.core.base import BaseStep
from wpipe_steps.core.decorators import step, to_obj

@step
class MySQLQueryStep(BaseStep):
    """
    Step for executing SQL queries on MySQL/MariaDB databases using wmysql.
    """

    def __init__(
        self, 
        host: str,
        user: str,
        password: str,
        database: str,
        query: str,
        params: Optional[Union[tuple, dict]] = None,
        port: int = 3306,
        fetch_results: bool = True,
        response_key: str = "mysql_results",
        name: Optional[str] = None,
        version: str = "v2.0"
    ):
        super().__init__(name, version)
        self.conn_params = {
            "host": host,
            "user": user,
            "password": password,
            "database": database,
            "port": port
        }
        self.query = query
        self.params = params
        self.fetch_results = fetch_results
        self.response_key = response_key

    @to_obj
    def __call__(self, data: Dict[str, Any]) -> Dict[str, Any]:
        wmysql = self.ensure_dependency("wmysql")
        try:
            with wmysql.Wmysql(**self.conn_params) as db:
                if self.fetch_results:
                    results = db.query(self.query, self.params)
                else:
                    results = db.execute(self.query, self.params)
            
            data[self.response_key] = {
                "success": True,
                "data": results
            }
            return data
        except Exception as e:
            data[self.response_key] = {"success": False, "error": str(e)}
            raise RuntimeError(f"Wmysql Query failed: {str(e)}")

mysql_query = MySQLQueryStep()
