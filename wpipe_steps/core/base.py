import importlib
from abc import ABC, abstractmethod
from typing import Any, Dict, Optional
from wpipe import step

class BaseStep(ABC):
    """
    Base class for all pre-built steps in wpipe-steps.
    Supports lazy loading and dependency validation.
    """
    
    def __init__(self, name: Optional[str] = None, version: str = "v1.0"):
        self.name = name or self.__class__.__name__
        self.version = version

    def ensure_dependency(self, module_name: str, install_name: Optional[str] = None):
        """
        Validates if a dependency is installed. 
        If not, raises an error with installation instructions.
        """
        try:
            return importlib.import_module(module_name)
        except ImportError:
            pkg = install_name or module_name
            raise ImportError(
                f"❌ The step '{self.name}' requires the '{module_name}' library.\n"
                f"👉 Please install it using: pip install {pkg}"
            )

    @abstractmethod
    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        The main logic of the step. Must be implemented by subclasses.
        """
        pass

    def __call__(self, data: Dict[str, Any]) -> Dict[str, Any]:
        return self.execute(data)

    @classmethod
    def as_step(cls, **kwargs):
        instance = cls(**kwargs)
        return step(name=instance.name, version=instance.version)(instance)
