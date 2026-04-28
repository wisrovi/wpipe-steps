import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))

from wpipe import Pipeline
from wpipe_steps.infrastructure import KubernetesPodCheckStep

def print_result(data):
    """Step to print the Kubernetes pod check result."""
    status = data.get("k8s_pod_status", {})
    if status.get("success"):
        print(f"\n✅ Pod Status Retrieved!")
        print(f"Pod: {status['pod']}")
        print(f"Namespace: {status['namespace']}")
        print(f"Phase: {status['phase']}")
        print(f"Pod IP: {status['pod_ip']}")
    else:
        print(f"\n❌ Check Failed: {status.get('error')}")
    return data

def main():
    pipeline = Pipeline(pipeline_name="K8s_Pod_Check_Demo", verbose=True)

    check_pod = KubernetesPodCheckStep.as_step(
        name="Check_Web_Pod",
        pod_name="web-app-pod",
        namespace="production"
    )

    pipeline.set_steps([
        check_pod,
        print_result
    ])

    print("🚀 Starting Kubernetes Pod Check Demo Pipeline...")
    pipeline.run({})

if __name__ == "__main__":
    main()
