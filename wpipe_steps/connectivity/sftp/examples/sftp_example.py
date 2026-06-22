import sys
from pathlib import Path

# Add project root to path for local development testing
sys.path.append(str(Path(__file__).parent.parent.parent))

from wpipe import Pipeline
from wpipe_steps.connectivity import SftpTransferStep

def main():
    pipeline = Pipeline(pipeline_name="SFTP_Demo", verbose=True)

    # Example of SFTP Upload
    # Note: Requires a valid SFTP server to run
    upload_file = SftpTransferStep.as_step(
        name="Backup_Upload",
        host="sftp.example.com",
        username="user123",
        password="password123",
        operation="upload",
        local_path="logs/today.log",
        remote_path="/backups/today.log"
    )

    pipeline.set_steps([
        upload_file,
        lambda d: print(f"\n📁 SFTP Status: {d['sftp_status']['message']}") or d
    ])

    # We skip execution if server is not real, but structure is correct
    print("🚀 SFTP Step defined. (Execution requires real server)")

if __name__ == "__main__":
    main()
