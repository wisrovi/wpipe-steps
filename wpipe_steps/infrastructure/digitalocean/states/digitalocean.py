from typing import Any, Dict, Optional, Literal
from wpipe_steps.core.base import BaseStep

class DigitalOceanDropletStep(BaseStep):
    """
    Step for managing DigitalOcean Droplets.
    Supports 'create', 'list', and 'destroy' operations.
    """
    
    def __init__(
        self, 
        token: str,
        operation: Literal["create", "list", "destroy"] = "list",
        name: Optional[str] = None,
        region: str = "nyc1",
        size: str = "s-1vcpu-1gb",
        image: str = "ubuntu-20-04-x64",
        droplet_id: Optional[int] = None,
        response_key: str = "digitalocean_status",
        step_name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__(step_name, version)
        self.token = token
        self.operation = operation
        self.droplet_name = name
        self.region = region
        self.size = size
        self.image = image
        self.droplet_id = droplet_id
        self.response_key = response_key

    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        do = self.ensure_dependency("digitalocean", "python-digitalocean")
        manager = do.Manager(token=self.token)
        
        try:
            result_info = {}
            if self.operation == "list":
                droplets = manager.get_all_droplets()
                result_info = [{"id": d.id, "name": d.name, "ip": d.ip_address} for d in droplets]
            elif self.operation == "create":
                droplet = do.Droplet(
                    token=self.token,
                    name=self.droplet_name,
                    region=self.region,
                    image=self.image,
                    size_slug=self.size,
                    backups=False
                )
                droplet.create()
                result_info = {"id": droplet.id, "status": "creating"}
            elif self.operation == "destroy":
                droplet = manager.get_droplet(self.droplet_id)
                droplet.destroy()
                result_info = {"status": "destroyed"}
            
            data[self.response_key] = {
                "success": True,
                "operation": self.operation,
                "data": result_info
            }
            return data
            
        except Exception as e:
            data[self.response_key] = {"success": False, "error": str(e)}
            raise RuntimeError(f"DigitalOcean operation failed: {str(e)}")
