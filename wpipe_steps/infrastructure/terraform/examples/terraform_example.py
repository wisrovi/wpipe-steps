import sys
from pathlib import Path

# Add project root to path for local development testing
sys.path.append(str(Path(__file__).parent.parent.parent))

from wpipe import Pipeline
from wpipe_steps.infrastructure import TerraformApplyStep

def main():
    pipeline = Pipeline(pipeline_name="Terraform_Infrastructure_Demo", verbose=True)

    # Example: Apply a terraform configuration
    tf_step = TerraformApplyStep.as_step(
        name="Deploy_Infra",
        working_dir="./terraform/aws_vpc",
        vars={"region": "us-east-1"}
    )

    pipeline.set_steps([
        tf_step,
        lambda d: print(f"\n🏗️ Terraform Success: {d['terraform_status']['success']}") or d
    ])

    print("🚀 Terraform Step defined. (Execution requires terraform installed)")

if __name__ == "__main__":
    main()
