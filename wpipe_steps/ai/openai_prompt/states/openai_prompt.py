from typing import Any, Dict, Optional
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep

@step(
    name="openai_prompt",
    version="v1.0",
    description="Direct queries to GPT-4/o1",
    tags=["ai", "openai", "sync"]
)
class OpenAiPromptStep(BaseStep):
    """
    Step for querying OpenAI GPT models.
    Requires 'openai' library.
    """
    
    def __init__(
        self,
        api_key: str,
        prompt: Optional[str] = None,
        prompt_key: Optional[str] = None,
        model: str = "gpt-4",
        response_key: str = "openai_status",
        name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__(name, version)
        self.api_key = api_key
        self.prompt = prompt
        self.prompt_key = prompt_key
        self.model = model
        self.response_key = response_key

    @to_obj
    def __call__(self, data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            openai = self.ensure_dependency("openai")
            
            client = openai.OpenAI(api_key=self.api_key)
            prompt_text = self.prompt or data.get(self.prompt_key, "Hello")
            
            response = client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt_text}]
            )
            
            data[self.response_key] = {
                "success": True,
                "prompt": prompt_text,
                "response": response.choices[0].message.content,
                "model": self.model
            }
            return data
            
        except Exception as e:
            data[self.response_key] = {"success": False, "error": str(e)}
            raise RuntimeError(f"OpenAI Prompt failed: {str(e)}")
