import sys
import os
from pathlib import Path

# Add project root to path for local development testing
sys.path.append(str(Path(__file__).parent.parent.parent))

from wpipe import Pipeline
from wpipe_steps.security import HashGeneratorStep

def main():
    pipeline = Pipeline(pipeline_name="Hash_Security_Demo", verbose=True)

    # Example: Hash a sensitive password from data
    hash_step = HashGeneratorStep.as_step(
        name="SHA256_Password",
        input_key="password",
        algorithm="sha256"
    )

    pipeline.set_steps([
        hash_step,
        lambda d: print(f"\n🔑 Hashed Password: {d['hash_result']['hash']}") or d
    ])

    print("🚀 Running Hash Demo Pipeline...")
    pipeline.run({"password": "my_super_secret_password"})

if __name__ == "__main__":
    main()
