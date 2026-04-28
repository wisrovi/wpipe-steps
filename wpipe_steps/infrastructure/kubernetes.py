from typing import Any, Dict, Optional
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep

@step(
    name="kubernetes_pod_check",
    version="v1.0",
    description="Monitor the status of a Kubernetes pod",
    tags=["infrastructure", "kubernetes", "sync"]
)
class KubernetesPodCheckStep(BaseStep):
    """
    Step for checking Kubernetes pod status.
    Requires 'kubernetes' library and valid kubeconfig.
    """

    def __init__(
        self,
        pod_name: str,
        namespace: str = "default",
        kubeconfig_path: Optional[str] = None,
        response_key: str = "k8s_pod_status",
        name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__(name, version)
        self.pod_name = pod_name
        self.namespace = namespace
        self.kubeconfig_path = kubeconfig_path
        self.response_key = response_key

    @to_obj
    def __call__(self, data: Dict[str, Any]) -> Dict[str, Any]:
        kubernetes = self.ensure_dependency("kubernetes")

        try:
            config = kubernetes.client.Configuration()

            if self.kubeconfig_path:
                kubernetes.config.load_kube_config_from_dict(config, self.kubeconfig_path)
            else:
                kubernetes.config.load_incluster_config()

            v1 = kubernetes.client.CoreV1Api()

            pod = v1.read_namespaced_pod(
                name=self.pod_name,
                namespace=self.namespace
            )

            data[self.response_key] = {
                "success": True,
                "pod": self.pod_name,
                "namespace": self.namespace,
                "phase": pod.status.phase,
                "pod_ip": pod.status.pod_ip
            }
            return data

        except Exception as e:
            data[self.response_key] = {"success": False, "error": str(e)}
            raise RuntimeError(f"Kubernetes Pod Check failed: {str(e)}")
