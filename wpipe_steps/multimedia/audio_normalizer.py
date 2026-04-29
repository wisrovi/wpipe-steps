from typing import Any, Dict, Optional
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep

@step(
    name="audio_normalizer",
    version="v1.0",
    description="Normalize audio volume",
    tags=["multimedia", "audio", "sync"]
)
class AudioNormalizerStep(BaseStep):
    """
    Step for normalizing audio volume.
    Requires 'pydub' library.
    """
    
    def __init__(
        self,
        input_path: str,
        output_path: Optional[str] = None,
        target_dbfs: float = -20.0,
        response_key: str = "audio_status",
        name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__(name, version)
        self.input_path = input_path
        self.output_path = output_path or input_path.replace(".", "_normalized.")
        self.target_dbfs = target_dbfs
        self.response_key = response_key

    @to_obj
    def __call__(self, data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            pydub = self.ensure_dependency("pydub")
            
            audio = pydub.AudioSegment.from_file(self.input_path)
            normalized = pydub.effects.normalize(audio, headroom=self.target_dbfs)
            
            normalized.export(self.output_path, format="wav")
            
            data[self.response_key] = {
                "success": True,
                "input": self.input_path,
                "output": self.output_path,
                "duration": len(normalized) / 1000.0
            }
            return data
            
        except Exception as e:
            data[self.response_key] = {"success": False, "error": str(e)}
            raise RuntimeError(f"Audio Normalizer failed: {str(e)}")
