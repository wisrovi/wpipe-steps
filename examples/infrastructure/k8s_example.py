import sys
from pathlib import Path

# Add project root to path for local development testing
sys.path.append(str(Path(__file__).parent.parent.parent))

from wpipe import Pipeline
from wpipe_steps.infrastructure import KubernetesPodCheckStep

def main():
    pipeline = Pipeline(pipeline_name="K8s_Infrastructure_Demo", verbose=True)

    # Example: Check pods in kube-system namespace
    k8s_step = KubernetesPodCheckStep.as_step(
        name="Check_System_Pods",
        namespace="kube-system"
    )

    pipeline.set_steps([
        k8s_step,
        lambda d: print(f"\n☸️ Pods found: {d['k8s_status']['count']}") or d
    ])

    print("🚀 Kubernetes Step defined. (Execution requires kubeconfig)")

if __name__ == "__main__":
    main()
