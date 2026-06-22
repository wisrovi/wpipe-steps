"""
SFTP Transfer Step - Secure file transfer using paramiko.
"""
from pydantic import BaseModel

import os
import paramiko
from typing import Any, Dict, Optional, Literal
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep


class SFTPContext(BaseModel):
    """Context for SFTP operations."""
    host: str
    username: str
    password: Optional[str] = None
    key_filename: Optional[str] = None
    port: int = 22
    operation: Literal["upload", "download"] = "upload"
    local_path: str = ""
    remote_path: str = ""


@step(
    name="sftp_transfer",
    version="v1.0",
    description="SFTP file transfer",
    tags=["connectivity", "sftp", "file", "sync"]
)
class SftpTransferStep(BaseStep):
    """Step for transferring files via SFTP (Secure File Transfer Protocol).
    
    Supports upload and download operations.
    """

    def __init__(
        self,
        response_key: str = "sftp_status",
        name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__()
        self.response_key = response_key
        self.name = name or "sftp_transfer"
        self.version = version

    @to_obj(SFTPContext)
    def __call__(self, data: SFTPContext) -> Dict[str, Any]:
        """Execute SFTP transfer operation.
        
        Args:
            data: Context containing host, username, password, key_filename, port, operation, local_path, remote_path.
            
        Returns:
            Dictionary with operation result.
        """
        transport = paramiko.Transport((data.host, data.port))
        try:
            if data.key_filename:
                key = paramiko.RSAKey.from_private_key_file(data.key_filename)
                transport.connect(username=data.username, pkey=key)
            else:
                transport.connect(username=data.username, password=data.password)
            
            sftp = paramiko.SFTPClient.from_transport(transport)
            
            if data.operation == "upload":
                sftp.put(data.local_path, data.remote_path)
                msg = f"File {data.local_path} uploaded to {data.remote_path}"
            else:
                sftp.get(data.remote_path, data.local_path)
                msg = f"File {data.remote_path} downloaded to {data.local_path}"
            
            sftp.close()
            transport.close()
            
            data[self.response_key] = {
                "success": True,
                "message": msg,
                "operation": data.operation
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
