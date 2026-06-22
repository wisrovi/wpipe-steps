from typing import Any, Dict, Optional
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep

@step(
    name="vault_secrets",
    version="v1.0",
    description="Retrieve secrets from HashiCorp Vault",
    tags=["security", "vault", "sync"]
)
class VaultSecretsStep(BaseStep):
    """
    Step for retrieving secrets from HashiCorp Vault.
    Requires 'hvac' library and a running Vault instance.
    """

    def __init__(
        self,
        vault_url: str,
        secret_path: str,
        token: Optional[str] = None,
        mount_point: str = "secret",
        response_key: str = "vault_secrets",
        name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__(name, version)
        self.vault_url = vault_url
        self.secret_path = secret_path
        self.token = token
        self.mount_point = mount_point
        self.response_key = response_key

    @to_obj
    def __call__(self, data: Dict[str, Any]) -> Dict[str, Any]:
        hvac = self.ensure_dependency("hvac")
        client = hvac.Client(url=self.vault_url, token=self.token or data.get("vault_token"))

        try:
            read_response = client.secrets.kv.v2.read_secret_version(
                path=self.secret_path,
                mount_point=self.mount_point
            )

            secrets = read_response['data']['data']

            data[self.response_key] = {
                "success": True,
                "path": self.secret_path,
                "data": secrets
            }
            return data

        except Exception as e:
            data[self.response_key] = {"success": False, "error": str(e)}
            raise RuntimeError(f"Vault Secret retrieval failed: {str(e)}")
