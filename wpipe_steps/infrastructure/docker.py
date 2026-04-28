from typing import Any, Dict, Optional
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep

@step(
    name="docker_container",
    version="v1.0",
    description="Manage Docker containers (start, stop, restart)",
    tags=["infrastructure", "docker", "sync"]
)
class DockerContainerStep(BaseStep):
    """
    Step for managing Docker containers.
    Requires 'docker' library.
    """

    def __init__(
        self,
        container_name: str,
        action: str = "start",  # start, stop, restart
        response_key: str = "docker_status",
        name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__(name, version)
        self.container_name = container_name
        self.action = action
        self.response_key = response_key

    @to_obj
    def __call__(self, data: Dict[str, Any]) -> Dict[str, Any]:
        docker = self.ensure_dependency("docker")

        try:
            client = docker.from_env()

            if self.action == "start":
                container = client.containers.get(self.container_name)
                container.start()
                status = "started"
            elif self.action == "stop":
                container = client.containers.get(self.container_name)
                container.stop()
                status = "stopped"
            elif self.action == "restart":
                container = client.containers.get(self.container_name)
                container.restart()
                status = "restarted"
            else:
                raise ValueError(f"Invalid action: {self.action}")

            data[self.response_key] = {
                "success": True,
                "container": self.container_name,
                "action": self.action,
                "status": status
            }
            return data

        except Exception as e:
            data[self.response_key] = {"success": False, "error": str(e)}
            raise RuntimeError(f"Docker Container operation failed: {str(e)}")
