from typing import Any, Dict, Optional, Literal
from wpipe_steps.core.base import BaseStep

class RedisCacheStep(BaseStep):
    """
    Step for interacting with Redis cache using wredis.
    """
    
    def __init__(
        self, 
        host: str = "localhost",
        port: int = 6379,
        db: int = 0,
        password: Optional[str] = None,
        operation: Literal["set", "get", "delete"] = "get",
        key: str = "",
        value_key: Optional[str] = None,
        response_key: str = "redis_data",
        name: Optional[str] = None,
        version: str = "v2.0"
    ):
        super().__init__(name, version)
        self.config = {
            "host": host,
            "port": port,
            "db": db,
            "password": password
        }
        self.operation = operation
        self.key = key
        self.value_key = value_key
        self.response_key = response_key

    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        # Dynamic import
        wredis = self.ensure_dependency("wredis")
        
        try:
            with wredis.Wredis(**self.config) as r:
                result = None
                if self.operation == "set":
                    value = data.get(self.value_key) if self.value_key else None
                    if value is not None:
                        r.set(self.key, value)
                        result = "OK"
                elif self.operation == "get":
                    result = r.get(self.key)
                elif self.operation == "delete":
                    result = r.delete(self.key)
            
            data[self.response_key] = {
                "success": True,
                "operation": self.operation,
                "key": self.key,
                "value": result
            }
            return data
        except Exception as e:
            data[self.response_key] = {"success": False, "error": str(e)}
            raise RuntimeError(f"Wredis operation failed: {str(e)}")
