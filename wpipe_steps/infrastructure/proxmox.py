from typing import Any, Dict, Optional, Literal
from wpipe_steps.core.base import BaseStep

class ProxmoxVMStep(BaseStep):
    """
    Step for managing Proxmox Virtual Machines.
    Supports 'start', 'stop', 'shutdown', and 'status' operations.
    """
    
    def __init__(
        self, 
        host: str,
        user: str,
        password: str,
        vmid: int,
        node: str,
        operation: Literal["start", "stop", "shutdown", "status"] = "status",
        verify_ssl: bool = False,
        response_key: str = "proxmox_status",
        name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__(name, version)
        self.host = host
        self.user = user
        self.password = password
        self.vmid = vmid
        self.node = node
        self.operation = operation
        self.verify_ssl = verify_ssl
        self.response_key = response_key

    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        proxmoxer = self.ensure_dependency("proxmoxer")
        from proxmoxer import ProxmoxAPI
        
        try:
            proxmox = ProxmoxAPI(
                self.host, 
                user=self.user, 
                password=self.password, 
                verify_ssl=self.verify_ssl
            )
            
            vm = proxmox.nodes(self.node).qemu(self.vmid)
            
            result_info = {}
            if self.operation == "status":
                result_info = vm.status.current.get()
            elif self.operation == "start":
                vm.status.start.post()
                result_info = {"action": "start_initiated"}
            elif self.operation == "stop":
                vm.status.stop.post()
                result_info = {"action": "stop_initiated"}
            
            data[self.response_key] = {
                "success": True,
                "vmid": self.vmid,
                "operation": self.operation,
                "info": result_info
            }
            return data
            
        except Exception as e:
            data[self.response_key] = {"success": False, "error": str(e)}
            raise RuntimeError(f"Proxmox operation failed: {str(e)}")
