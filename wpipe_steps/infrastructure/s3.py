from typing import Any, Dict, Optional
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep

@step(
    name="s3_upload",
    version="v1.0",
    description="Upload files to AWS S3 buckets",
    tags=["infrastructure", "aws", "s3", "sync"]
)
class S3BucketUploadStep(BaseStep):
    """
    Step for uploading files to AWS S3 buckets.
    Requires 'boto3' library and valid AWS credentials.
    """

    def __init__(
        self,
        bucket_name: str,
        local_path: str,
        object_name: Optional[str] = None,
        aws_access_key: Optional[str] = None,
        aws_secret_key: Optional[str] = None,
        region_name: Optional[str] = None,
        response_key: str = "s3_upload_status",
        name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__(name, version)
        self.bucket_name = bucket_name
        self.local_path = local_path
        self.object_name = object_name or local_path
        self.aws_access_key = aws_access_key
        self.aws_secret_key = aws_secret_key
        self.region_name = region_name
        self.response_key = response_key

    @to_obj
    def __call__(self, data: Dict[str, Any]) -> Dict[str, Any]:
        boto3 = self.ensure_dependency("boto3")

        try:
            s3_client = boto3.client(
                's3',
                aws_access_key_id=self.aws_access_key or data.get("aws_access_key"),
                aws_secret_access_key=self.aws_secret_key or data.get("aws_secret_key"),
                region_name=self.region_name or data.get("aws_region")
            )

            s3_client.upload_file(self.local_path, self.bucket_name, self.object_name)

            data[self.response_key] = {
                "success": True,
                "bucket": self.bucket_name,
                "object": self.object_name,
                "local_file": self.local_path
            }
            return data

        except Exception as e:
            data[self.response_key] = {"success": False, "error": str(e)}
            raise RuntimeError(f"S3 Upload failed: {str(e)}")
