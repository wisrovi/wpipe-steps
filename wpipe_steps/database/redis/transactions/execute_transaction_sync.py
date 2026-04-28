"""
Redis transaction operations - execute_transaction (synchronous).
"""

from typing import Any, Dict, List, Optional, Tuple
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.sync import RedisTransactionManager


class ExecuteTransactionContext(BaseModel):
    """Context for executing a transaction in Redis."""
    commands: List[Tuple[str, List[str]]]


@step(
    name="redis_transaction_execute_sync",
    version="v1.0",
    description="Execute transaction in Redis (synchronous)",
    tags=["redis", "transaction", "write", "sync"]
)
class RedisTransactionExecuteSync(BaseStep):
    """Execute a transaction in Redis (synchronous)."""

    def __init__(
        self,
        host: str = "192.168.1.84",
        port: int = 6379,
        db: int = 0,
        name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__()
        self.host = host
        self.port = port
        self.db = db
        self.name = name or "redis_transaction_execute_sync"
        self.version = version
        self.manager = RedisTransactionManager(host=host, port=port, db=db)

    @to_obj(ExecuteTransactionContext)
    def __call__(self, data: ExecuteTransactionContext) -> Dict[str, Any]:
        """Execute the execute_transaction operation.

        Args:
            data: Context containing commands.

        Returns:
            Dictionary with operation result.
        """
        try:
            result = self.manager.execute_transaction(data.commands)
            return {
                "success": True,
                "operation": "execute_transaction",
                "results": result
            }
        except Exception as e:
            return {
                "success": False,
                "operation": "execute_transaction",
                "error": str(e)
            }
