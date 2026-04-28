import pymysql
from typing import Any, Dict, Optional, List, Union
from wpipe_steps.core.base import BaseStep

class MySQLQueryStep(BaseStep):
    """
    Step for executing SQL queries on MySQL/MariaDB databases.
    Supports SELECT, INSERT, UPDATE, and DELETE.
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
        version: str = "v1.0"
    ):
        super().__init__(name, version)
        self.config = {
            "host": host,
            "user": user,
            "password": password,
            "database": database,
            "port": port,
            "cursorclass": pymysql.cursors.DictCursor
        }
        self.query = query
        self.params = params
        self.fetch_results = fetch_results
        self.response_key = response_key

    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        connection = pymysql.connect(**self.config)
        try:
            with connection.cursor() as cursor:
                cursor.execute(self.query, self.params)
                
                if self.fetch_results:
                    results = cursor.fetchall()
                else:
                    results = {"affected_rows": cursor.rowcount}
                
                connection.commit()
                
            data[self.response_key] = {
                "success": True,
                "data": results
            }
            
            return data
            
        except Exception as e:
            data[self.response_key] = {
                "success": False,
                "error": str(e)
            }
            raise RuntimeError(f"MySQL Query failed: {str(e)}")
        finally:
            connection.close()
