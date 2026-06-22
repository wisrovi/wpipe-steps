from typing import Any, Dict, Optional
from wpipe_steps.core.base import BaseStep


class HFConversationalStep(BaseStep):
    def __init__(self, name=None, version="v1.0", model_name="facebook/blenderbot-400M-distill", device="cpu", response_key="conversation"):
        super().__init__(name, version)
        self.model_name = model_name
        self.device = device
        self.response_key = response_key
    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        if pipe is None:
            from transformers import pipeline
            pipe = pipeline(task="conversational", model=self.model_name, device=self.device, local_files_only=True)
        text = data.get("text", "")
        if not text:
            data[self.response_key] = {"error": "No text"}
            return data
        from transformers import Conversation
        conv = Conversation(text)
        result = pipe(conv)
        data[self.response_key] = {"input": text, "response": result.generated_responses[-1]}
        return data
