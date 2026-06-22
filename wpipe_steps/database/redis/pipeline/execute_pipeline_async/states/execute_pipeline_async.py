"""
Redis pipeline operations - execute_pipeline (asynchronous).
"""

from typing import Any, Dict, List, Optional, Tuple
from pydantic import BaseModel
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep
from wredis.aio import RedisPipelineManager


class ExecutePipelineContext(BaseModel):
    """Context for executing a pipeline in Redis."""
    commands: List[Tuple[str, List[str]]]


@step(
    name="redis_pipeline_execute_async",
    version="v1.0",
    description="Execute pipeline in Redis (asynchronous)",
    tags=["redis", "pipeline", "write", "async"]
)
class RedisPipelineExecuteAsync(BaseStep):
    """Execute a pipeline in Redis (asynchronous)."""

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
        self.name = name or "redis_pipeline_execute_async"
        self.version = version

    @to_obj(ExecutePipelineContext)
    async def __call__(self, data: ExecutePipelineContext) -> Dict[str, Any]:
        """Execute the execute_pipeline operation asynchronously.

        Args:
            data: Context containing commands.

        Returns:
            Dictionary with operation result.
        """
        try:
            manager = RedisPipelineManager(host=self.host, port=self.port, db=self.db)
            result = await manager.execute_pipeline(data.commands)
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
