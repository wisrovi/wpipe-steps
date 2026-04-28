from abc import ABC, abstractmethod
from typing import Any, Dict, Optional
from wpipe import step

class BaseStep(ABC):
    """
    Base class for all pre-built steps in wpipe-steps.
    Provides common functionality for logging and execution context.
    """
    
    def __init__(self, name: Optional[str] = None, version: str = "v1.0"):
        self.name = name or self.__class__.__name__
        self.version = version

    @abstractmethod
    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        The main logic of the step. Must be implemented by subclasses.
        """
        pass

    def __call__(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Makes the instance callable, allowing it to be used directly in pipelines.
        """
        return self.execute(data)

    @classmethod
    def as_step(cls, **kwargs):
        """
        Factory method to return an instance decorated as a wpipe step.
        """
        instance = cls(**kwargs)
        return step(name=instance.name, version=instance.version)(instance)
