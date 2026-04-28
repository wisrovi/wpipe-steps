import sys
from pathlib import Path

# Add project root to path for local development testing
sys.path.append(str(Path(__file__).parent.parent.parent))

from wpipe import Pipeline
from wpipe_steps.infrastructure import S3BucketUploadStep

def main():
    pipeline = Pipeline(pipeline_name="S3_Infrastructure_Demo", verbose=True)

    # Example: Upload a log file to S3
    s3_step = S3BucketUploadStep.as_step(
        name="Backup_to_S3",
        bucket_name="my-app-backups",
        local_path="results.csv",
        aws_access_key="AKIA...", # Template only
        aws_secret_key="secret..."
    )

    pipeline.set_steps([
        s3_step,
        lambda d: print(f"\n☁️ S3 Upload Status: {d['s3_upload_status']['success']}") or d
    ])

    print("🚀 S3 Step defined. (Execution requires AWS credentials)")

if __name__ == "__main__":
    main()
