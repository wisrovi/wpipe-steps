"""
Redis pipeline operations - execute_pipeline (synchronous).
"""

from typing import Any, Dict, List, Optional, Tuple
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.sync import RedisPipelineManager


class ExecutePipelineContext(BaseModel):
    """Context for executing a pipeline in Redis."""
    commands: List[Tuple[str, List[str]]]


@step(
    name="redis_pipeline_execute_sync",
    version="v1.0",
    description="Execute pipeline in Redis (synchronous)",
    tags=["redis", "pipeline", "write", "sync"]
)
class RedisPipelineExecuteSync(BaseStep):
    """Execute a pipeline in Redis (synchronous)."""

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
        self.name = name or "redis_pipeline_execute_sync"
        self.version = version
        self.manager = RedisPipelineManager(host=host, port=port, db=db)

    @to_obj(ExecutePipelineContext)
    def __call__(self, data: ExecutePipelineContext) -> Dict[str, Any]:
        """Execute the execute_pipeline operation.

        Args:
            data: Context containing commands.

        Returns:
            Dictionary with operation result.
        """
        try:
            result = self.manager.execute_pipeline(data.commands)
            return {
                "success": True,
                "operation": "execute_pipeline",
                "results": result
            }
        except Exception as e:
            return {
                "success": False,
                "operation": "execute_pipeline",
                "error": str(e)
            }
