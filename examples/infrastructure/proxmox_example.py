import sys
from pathlib import Path

# Add project root to path for local development testing
sys.path.append(str(Path(__file__).parent.parent.parent))

from wpipe import Pipeline
from wpipe_steps.infrastructure import ProxmoxVMStep

def main():
    pipeline = Pipeline(pipeline_name="Proxmox_Infrastructure_Demo", verbose=True)

    # Example: Check status of VM 100
    proxmox_step = ProxmoxVMStep.as_step(
        name="VM_Status_Check",
        host="192.168.1.50",
        user="root@pam",
        password="secret_password",
        vmid=100,
        node="pve-node-1",
        operation="status"
    )

    pipeline.set_steps([
        proxmox_step,
        lambda d: print(f"\n🖥️ VM Status: {d['proxmox_status']['info'].get('status')}") or d
    ])

    print("🚀 Proxmox Step defined. (Execution requires real Proxmox server)")

if __name__ == "__main__":
    main()
