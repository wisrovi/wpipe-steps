from dataclasses import dataclass
from loguru import logger
import yaml
from typing import Dict, Any
from wpipe import step, to_obj
import os


@dataclass
class InputContext:
    yaml_path: str = ""


class NotFoundError(Exception):
    pass


@step(
    name="LoadYaml",
    version="v1.0",
    description="Loads a YAML configuration file",
)
class LoadYaml:
    """
    Step to load a YAML configuration file.
    """

    def __init__(
        self,
        yaml_path: str,
    ):
        self.yaml_path = yaml_path

    @to_obj(InputContext)
    def __call__(self, data: InputContext) -> Dict[str, Any]:

        if not self.yaml_path and len(data.yaml_path) > 0:
            self.yaml_path = data.yaml_path

        if not self.yaml_path or os.path.exists(self.yaml_path) == False:
            raise NotFoundError(f"YAML file not found at path: {self.yaml_path}")

        try:
            with open(self.yaml_path) as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            logger.warning(f"Config not found at '{self.yaml_path}', using defaults.")
            return {}
