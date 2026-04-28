from typing import Any, Dict, Optional
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep

@step(
    name="digitalocean_droplet",
    version="v1.0",
    description="Manage DigitalOcean droplets via API",
    tags=["infrastructure", "digitalocean", "sync"]
)
class DigitalOceanDropletStep(BaseStep):
    """
    Step for managing DigitalOcean droplets.
    Requires 'python-digitalocean' library and API token.
    """

    def __init__(
        self,
        token: str,
        droplet_id: Optional[int] = None,
        action: str = "list",  # list, create, delete, reboot, shutdown
        response_key: str = "do_droplet_status",
        name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__(name, version)
        self.token = token
        self.droplet_id = droplet_id
        self.action = action
        self.response_key = response_key

    @to_obj
    def __call__(self, data: Dict[str, Any]) -> Dict[str, Any]:
        digitalocean = self.ensure_dependency("digitalocean")

        try:
            digitalocean.Droplet.BEARER = self.token

            if self.action == "list":
                droplets = digitalocean.Droplet().load_all()
                result = [{"id": d.id, "name": d.name, "status": d.status} for d in droplets]
            elif self.action == "create":
                droplet = digitalocean.Droplet()
                # Configuration from data
                droplet.name = data.get("droplet_name", "wpipe-droplet")
                droplet.region = data.get("region", "nyc3")
                droplet.size = data.get("size", "s-1vcpu-1gb")
                droplet.image = data.get("image", "ubuntu-20-04-x64")
                droplet.create()
                result = {"id": droplet.id, "name": droplet.name, "status": "creating"}
            elif self.action == "delete" and self.droplet_id:
                droplet = digitalocean.Droplet(id=self.droplet_id)
                droplet.destroy()
                result = {"id": self.droplet_id, "status": "deleted"}
            else:
                raise ValueError(f"Invalid action or missing droplet_id")

            data[self.response_key] = {
                "success": True,
                "action": self.action,
                "result": result
            }
            return data

        except Exception as e:
            data[self.response_key] = {"success": False, "error": str(e)}
            raise RuntimeError(f"DigitalOcean Droplet operation failed: {str(e)}")
