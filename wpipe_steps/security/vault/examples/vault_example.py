import sys
from pathlib import Path

# Add project root to path for local development testing
sys.path.append(str(Path(__file__).parent.parent.parent))

from wpipe import Pipeline
from wpipe_steps.security import VaultSecretsStep

def main():
    pipeline = Pipeline(pipeline_name="Vault_Security_Demo", verbose=True)

    # Example: Retrieve DB credentials from Vault
    vault_step = VaultSecretsStep.as_step(
        name="Get_DB_Secrets",
        vault_url="http://localhost:8200",
        secret_path="database/config",
        token="root" # Template only
    )

    pipeline.set_steps([
        vault_step,
        lambda d: print(f"\n🔑 Credentials retrieved for: {d['vault_secrets']['path']}") or d
    ])

    print("🚀 Vault Step defined. (Execution requires real Vault instance)")

if __name__ == "__main__":
    main()
