from typing import Any, Dict, Optional
from wpipe_steps.core.base import BaseStep

class KubernetesPodCheckStep(BaseStep):
    """
    Step for checking the status of Kubernetes Pods.
    Requires 'kubernetes' library and a valid kubeconfig.
    """
    
    def __init__(
        self, 
        namespace: str = "default",
        label_selector: Optional[str] = None,
        response_key: str = "k8s_status",
        name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__(name, version)
        self.namespace = namespace
        self.label_selector = label_selector
        self.response_key = response_key

    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        k8s = self.ensure_dependency("kubernetes")
        from kubernetes import client, config
        
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()
            
            pods = v1.list_namespaced_pod(
                self.namespace, 
                label_selector=self.label_selector or ""
            )
            
            pod_list = []
            for pod in pods.items:
                pod_list.append({
                    "name": pod.metadata.name,
                    "status": pod.status.phase,
                    "ip": pod.status.pod_ip
                })
            
            data[self.response_key] = {
                "success": True,
                "namespace": self.namespace,
                "pods": pod_list,
                "count": len(pod_list)
            }
            return data
            
        except Exception as e:
            data[self.response_key] = {"success": False, "error": str(e)}
            raise RuntimeError(f"Kubernetes Pod Check failed: {str(e)}")
