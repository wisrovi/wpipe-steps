# ☁️ Infrastructure Examples

This directory contains examples of how to interact with cloud and infrastructure services.

## Examples included:

### 1. AWS S3 Upload (`s3_example.py`)
Shows how to upload local files to an AWS S3 bucket using `S3BucketUploadStep` (Requires `boto3`).

### 2. Docker Management (`docker_example.py`)
Demonstrates how to run and manage Docker containers using `DockerContainerStep` (Requires `docker`).

### 3. Kubernetes Pod Check (`k8s_example.py`)
Demonstrates how to list and check status of Kubernetes Pods using `KubernetesPodCheckStep` (Requires `kubernetes`).

### 4. Terraform Apply (`terraform_example.py`)
Demonstrates how to apply Terraform configurations using `TerraformApplyStep` (Requires `python-terraform`).

### 5. Proxmox VM Management (`proxmox_example.py`)
Demonstrates how to control Proxmox virtual machines via API using `ProxmoxVMStep` (Requires `proxmoxer`).

---
*Note: Cloud examples require valid API keys or configuration files.*
