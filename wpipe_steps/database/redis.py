import redis
from typing import Any, Dict, Optional, Literal, Union
from wpipe_steps.core.base import BaseStep

class RedisCacheStep(BaseStep):
    """
    Step for interacting with Redis cache.
    Supports 'set', 'get', and 'delete' operations.
    """
    
    def __init__(
        self, 
        host: str = "localhost",
        port: int = 6379,
        db: int = 0,
        password: Optional[str] = None,
        operation: Literal["set", "get", "delete"] = "get",
        key: str = "",
        value_key: Optional[str] = None, # Key in 'data' to get value from (for 'set')
        response_key: str = "redis_data",
        name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__(name, version)
        self.config = {
            "host": host,
            "port": port,
            "db": db,
            "password": password,
            "decode_responses": True
        }
        self.operation = operation
        self.key = key
        self.value_key = value_key
        self.response_key = response_key

    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        client = redis.Redis(**self.config)
        try:
            result = None
            if self.operation == "set":
                value = data.get(self.value_key) if self.value_key else None
                if value is not None:
                    client.set(self.key, str(value))
                    result = "OK"
            elif self.operation == "get":
                result = client.get(self.key)
            elif self.operation == "delete":
                result = client.delete(self.key)
            
            data[self.response_key] = {
                "success": True,
                "operation": self.operation,
                "key": self.key,
                "value": result
            }
            
            return data
            
        except Exception as e:
            data[self.response_key] = {
                "success": False,
                "error": str(e)
            }
            raise RuntimeError(f"Redis operation failed: {str(e)}")
        finally:
            client.close()
