from typing import Any, Dict, Optional
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep

@step(
    name="terraform_apply",
    version="v1.0",
    description="Execute Terraform apply for infrastructure changes",
    tags=["infrastructure", "terraform", "sync"]
)
class TerraformApplyStep(BaseStep):
    """
    Step for running Terraform apply.
    Requires 'python-terraform' library and Terraform installed.
    """

    def __init__(
        self,
        working_dir: str,
        variables: Optional[Dict[str, Any]] = None,
        auto_approve: bool = False,
        response_key: str = "terraform_status",
        name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__(name, version)
        self.working_dir = working_dir
        self.variables = variables or {}
        self.auto_approve = auto_approve
        self.response_key = response_key

    @to_obj
    def __call__(self, data: Dict[str, Any]) -> Dict[str, Any]:
        terraform = self.ensure_dependency("terraform", "python-terraform")

        try:
            tf = terraform.Terraform(working_dir=self.working_dir)

            return_code, stdout, stderr = tf.apply(
                auto_approve=self.auto_approve,
                **self.variables
            )

            data[self.response_key] = {
                "success": return_code == 0,
                "return_code": return_code,
                "stdout": stdout,
                "stderr": stderr
            }
            return data

        except Exception as e:
            data[self.response_key] = {"success": False, "error": str(e)}
            raise RuntimeError(f"Terraform Apply failed: {str(e)}")
