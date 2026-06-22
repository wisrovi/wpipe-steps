import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))

from wpipe import Pipeline
from wpipe_steps.infrastructure import S3BucketUploadStep

def print_result(data):
    """Step to print the S3 upload result."""
    status = data.get("s3_upload_status", {})
    if status.get("success"):
        print(f"\n✅ Upload Successful!")
        print(f"Bucket: {status['bucket']}")
        print(f"Object: {status['object']}")
    else:
        print(f"\n❌ Upload Failed: {status.get('error')}")
    return data

def main():
    pipeline = Pipeline(pipeline_name="S3_Upload_Demo", verbose=True)

    upload = S3BucketUploadStep.as_step(
        name="Upload_to_S3",
        bucket_name="my-bucket",
        local_path="./test.txt",
        aws_access_key="YOUR_ACCESS_KEY",
        aws_secret_key="YOUR_SECRET_KEY"
    )

    pipeline.set_steps([
        upload,
        print_result
    ])

    print("🚀 Starting S3 Upload Demo Pipeline...")
    pipeline.run({})

if __name__ == "__main__":
    main()
