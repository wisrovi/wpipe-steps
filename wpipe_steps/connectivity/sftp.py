import os
import paramiko
from typing import Any, Dict, Optional, Literal
from wpipe_steps.core.base import BaseStep

class SftpTransferStep(BaseStep):
    """
    Step for transferring files via SFTP (Secure File Transfer Protocol).
    Supports upload and download operations.
    """
    
    def __init__(
        self, 
        host: str,
        username: str,
        password: Optional[str] = None,
        key_filename: Optional[str] = None,
        port: int = 22,
        operation: Literal["upload", "download"] = "upload",
        local_path: str = "",
        remote_path: str = "",
        response_key: str = "sftp_status",
        name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__(name, version)
        self.host = host
        self.username = username
        self.password = password
        self.key_filename = key_filename
        self.port = port
        self.operation = operation
        self.local_path = local_path
        self.remote_path = remote_path
        self.response_key = response_key

    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        transport = paramiko.Transport((self.host, self.port))
        try:
            if self.key_filename:
                key = paramiko.RSAKey.from_private_key_file(self.key_filename)
                transport.connect(username=self.username, pkey=key)
            else:
                transport.connect(username=self.username, password=self.password)
            
            sftp = paramiko.SFTPClient.from_transport(transport)
            
            if self.operation == "upload":
                sftp.put(self.local_path, self.remote_path)
                msg = f"File {self.local_path} uploaded to {self.remote_path}"
            else:
                sftp.get(self.remote_path, self.local_path)
                msg = f"File {self.remote_path} downloaded to {self.local_path}"
            
            sftp.close()
            transport.close()
            
            data[self.response_key] = {
                "success": True,
                "message": msg,
                "operation": self.operation
            }
            
            return data
            
        except Exception as e:
            if transport.is_active():
                transport.close()
            data[self.response_key] = {
                "success": False,
                "error": str(e)
            }
            raise RuntimeError(f"SFTP Transfer failed: {str(e)}")
