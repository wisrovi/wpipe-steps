from typing import Any, Dict, Optional
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep

@step(
    name="proxmox_vm",
    version="v1.0",
    description="Control virtual machines in Proxmox",
    tags=["infrastructure", "proxmox", "sync"]
)
class ProxmoxVMStep(BaseStep):
    """
    Step for controlling Proxmox VMs.
    Requires 'proxmoxer' library.
    """

    def __init__(
        self,
        host: str,
        user: str,
        password: str,
        node: str,
        vm_id: int,
        action: str = "status",  # start, stop, restart, status
        verify_ssl: bool = False,
        response_key: str = "proxmox_vm_status",
        name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__(name, version)
        self.host = host
        self.user = user
        self.password = password
        self.node = node
        self.vm_id = vm_id
        self.action = action
        self.verify_ssl = verify_ssl
        self.response_key = response_key

    @to_obj
    def __call__(self, data: Dict[str, Any]) -> Dict[str, Any]:
        proxmoxer = self.ensure_dependency("proxmoxer")

        try:
            proxmox = proxmoxer.ProxmoxAPI(
                self.host,
                user=self.user,
                password=self.password,
                verify_ssl=self.verify_ssl
            )

            vm = proxmox.nodes(self.node).qemu(self.vm_id)

            if self.action == "start":
                result = vm.status.start.post()
            elif self.action == "stop":
                result = vm.status.stop.post()
            elif self.action == "restart":
                vm.status.stop.post()
                result = vm.status.start.post()
            else:  # status
                result = vm.status.current.get()

            data[self.response_key] = {
                "success": True,
                "vm_id": self.vm_id,
                "node": self.node,
                "action": self.action,
                "result": result
            }
            return data

        except Exception as e:
            data[self.response_key] = {"success": False, "error": str(e)}
            raise RuntimeError(f"Proxmox VM operation failed: {str(e)}")
