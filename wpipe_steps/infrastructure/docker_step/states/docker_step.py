from typing import Any, Dict, Optional, Literal
from wpipe_steps.core.base import BaseStep

class DockerContainerStep(BaseStep):
    """
    Step for managing Docker containers.
    Supports 'run', 'start', 'stop', and 'remove' operations.
    """
    
    def __init__(
        self, 
        image: str,
        operation: Literal["run", "start", "stop", "remove"] = "run",
        container_name: Optional[str] = None,
        command: Optional[str] = None,
        detach: bool = True,
        response_key: str = "docker_status",
        name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__(name, version)
        self.image = image
        self.operation = operation
        self.container_name = container_name
        self.command = command
        self.detach = detach
        self.response_key = response_key

    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        docker = self.ensure_dependency("docker")
        client = docker.from_env()
        
        try:
            result_info = {}
            if self.operation == "run":
                container = client.containers.run(
                    self.image, 
                    command=self.command, 
                    name=self.container_name, 
                    detach=self.detach
                )
                result_info = {"id": container.id, "status": container.status}
            elif self.operation == "stop":
                container = client.containers.get(self.container_name)
                container.stop()
                result_info = {"status": "stopped"}
            # Add other ops...
            
            data[self.response_key] = {
                "success": True,
                "operation": self.operation,
                "info": result_info
            }
            return data
            
        except Exception as e:
            data[self.response_key] = {"success": False, "error": str(e)}
            raise RuntimeError(f"Docker operation failed: {str(e)}")
