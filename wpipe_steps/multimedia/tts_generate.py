from typing import Any, Dict, Optional
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep

@step(
    name="tts_generate",
    version="v1.0",
    description="Text to speech with natural voices",
    tags=["multimedia", "tts", "audio", "sync"]
)
class TtsGenerateStep(BaseStep):
    """
    Step for converting text to speech.
    Requires 'gtts' library (Google Text-to-Speech).
    """
    
    def __init__(
        self,
        text: Optional[str] = None,
        text_key: Optional[str] = None,
        output_path: str = "output.mp3",
        language: str = "en",
        response_key: str = "tts_status",
        name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__(name, version)
        self.text = text
        self.text_key = text_key
        self.output_path = output_path
        self.language = language
        self.response_key = response_key

    @to_obj
    def __call__(self, data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            gtts = self.ensure_dependency("gtts")
            
            text = self.text or data.get(self.text_key, "Hello World")
            tts = gtts.gTTS(text=text, lang=self.language)
            tts.save(self.output_path)
            
            data[self.response_key] = {
                "success": True,
                "text": text,
                "output": self.output_path,
                "language": self.language
            }
            return data
            
        except Exception as e:
            data[self.response_key] = {"success": False, "error": str(e)}
            raise RuntimeError(f"TTS Generate failed: {str(e)}")
