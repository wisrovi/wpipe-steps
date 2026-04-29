from typing import Any, Dict, Optional
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep

@step(
    name="text_translator",
    version="v1.0",
    description="Integration with Google/DeepL Translate",
    tags=["data", "translate", "sync"]
)
class TextTranslatorStep(BaseStep):
    """
    Step for translating text using Google Translate (free).
    """
    
    def __init__(
        self,
        text: Optional[str] = None,
        text_key: Optional[str] = None,
        target_language: str = "en",
        response_key: str = "translation_status",
        name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__(name, version)
        self.text = text
        self.text_key = text_key
        self.target_language = target_language
        self.response_key = response_key

    @to_obj
    def __call__(self, data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            from googletrans import Translator
            
            text = self.text or data.get(self.text_key, "")
            translator = Translator()
            result = translator.translate(text, dest=self.target_language)
            
            data[self.response_key] = {
                "success": True,
                "original": text,
                "translated": result.text,
                "src_lang": result.src,
                "dest_lang": self.target_language
            }
            return data
            
        except Exception as e:
            data[self.response_key] = {"success": False, "error": str(e)}
            raise RuntimeError(f"Text Translator failed: {str(e)}")
