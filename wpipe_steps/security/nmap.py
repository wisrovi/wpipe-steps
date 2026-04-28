from typing import Any, Dict, Optional
from wpipe_steps.core.base import BaseStep

class NmapScanStep(BaseStep):
    """
    Step for performing Nmap port scans.
    Requires nmap binary installed on the system and python-nmap library.
    """
    
    def __init__(
        self, 
        target: str,
        ports: str = "22,80,443",
        arguments: str = "-sV",
        response_key: str = "nmap_scan",
        name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__(name, version)
        self.target = target
        self.ports = ports
        self.arguments = arguments
        self.response_key = response_key

    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        nmap = self.ensure_dependency("nmap", "python-nmap")
        nm = nmap.PortScanner()
        
        try:
            nm.scan(self.target, self.ports, arguments=self.arguments)
            
            scan_results = []
            for host in nm.all_hosts():
                host_info = {
                    "host": host,
                    "hostname": nm[host].hostname(),
                    "state": nm[host].state(),
                    "protocols": []
                }
                for proto in nm[host].all_protocols():
                    ports = nm[host][proto].keys()
                    host_info["protocols"].append({
                        "protocol": proto,
                        "ports": [{port: nm[host][proto][port]} for port in ports]
                    })
                scan_results.append(host_info)
            
            data[self.response_key] = {
                "success": True,
                "target": self.target,
                "results": scan_results
            }
            return data
            
        except Exception as e:
            data[self.response_key] = {"success": False, "error": str(e)}
            raise RuntimeError(f"Nmap Scan failed: {str(e)}")
