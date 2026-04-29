from typing import Any, Dict, Optional
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep

@step(
    name="whisper_transcribe",
    version="v1.0",
    description="Transcribe audio to text using Whisper AI",
    tags=["multimedia", "audio", "whisper", "ai", "sync"]
)
class WhisperTranscribeStep(BaseStep):
    """
    Step for transcribing audio using OpenAI Whisper.
    Requires 'openai-whisper' library.
    """
    
    def __init__(
        self,
        audio_path: str,
        model_size: str = "base",
        language: Optional[str] = None,
        response_key: str = "whisper_status",
        name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__(name, version)
        self.audio_path = audio_path
        self.model_size = model_size
        self.language = language
        self.response_key = response_key

    @to_obj
    def __call__(self, data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            whisper = self.ensure_dependency("whisper", "openai-whisper")
            
            model = whisper.load_model(self.model_size)
            
            result = model.transcribe(
                self.audio_path,
                language=self.language
            )
            
            data[self.response_key] = {
                "success": True,
                "text": result["text"],
                "language": result.get("language", self.language),
                "audio": self.audio_path
            }
            return data
            
        except Exception as e:
            data[self.response_key] = {"success": False, "error": str(e)}
            raise RuntimeError(f"Whisper Transcription failed: {str(e)}")
