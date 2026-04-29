from typing import Any, Dict, Optional
import subprocess
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep

@step
class ShellExecStep(BaseStep):
    """
    Step for executing shell commands.
    """
    def __init__(self, command: str, name: Optional[str] = None, version: str = "v1.0", response_key: str = "shell_status"):
        super().__init__(name, version)
        self.command = command
        self.response_key = response_key

    @to_obj
    def __call__(self, data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            result = subprocess.run(self.command, shell=True, capture_output=True, text=True, check=True)
            data[self.response_key] = {
                "success": True,
                "stdout": result.stdout.strip(),
                "stderr": result.stderr.strip(),
                "returncode": result.returncode
            }
        except subprocess.CalledProcessError as e:
            data[self.response_key] = {
                "success": False,
                "stdout": e.stdout.strip(),
                "stderr": e.stderr.strip(),
                "returncode": e.returncode,
                "error": str(e)
            }
        
        return data
