import subprocess
import os
from typing import Any, Dict, Optional
from wpipe_steps.core.base import BaseStep

class TerraformApplyStep(BaseStep):
    """
    Step for executing Terraform apply.
    Requires terraform binary installed on the system and python-terraform library.
    """
    
    def __init__(
        self, 
        working_dir: str,
        vars: Optional[Dict[str, Any]] = None,
        auto_approve: bool = True,
        response_key: str = "terraform_status",
        name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__(name, version)
        self.working_dir = working_dir
        self.vars = vars or {}
        self.auto_approve = auto_approve
        self.response_key = response_key

    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        tf_lib = self.ensure_dependency("python_terraform", "python-terraform")
        from python_terraform import Terraform
        
        try:
            tf = Terraform(working_dir=self.working_dir)
            
            # 1. Init
            tf.init()
            
            # 2. Apply
            return_code, stdout, stderr = tf.apply(
                skip_plan=True, 
                vars=self.vars, 
                capture_output=True,
                auto_approve=self.auto_approve
            )
            
            data[self.response_key] = {
                "success": return_code == 0,
                "stdout": stdout,
                "stderr": stderr,
                "return_code": return_code
            }
            return data
            
        except Exception as e:
            data[self.response_key] = {"success": False, "error": str(e)}
            raise RuntimeError(f"Terraform Apply failed: {str(e)}")
        finally:
            pass
