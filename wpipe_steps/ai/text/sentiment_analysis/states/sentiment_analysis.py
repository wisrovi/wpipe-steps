from typing import Any, Dict, Optional
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep

@step(
    name="sentiment_analysis",
    version="v1.0",
    description="Analyze tone in user comments",
    tags=["ai", "sentiment", "nlp", "sync"]
)
class SentimentAnalysisStep(BaseStep):
    """
    Step for analyzing sentiment of text.
    Requires 'textblob' or 'vaderSentiment' library.
    """
    
    def __init__(
        self,
        text: Optional[str] = None,
        text_key: Optional[str] = None,
        response_key: str = "sentiment_status",
        name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__(name, version)
        self.text = text
        self.text_key = text_key
        self.response_key = response_key

    @to_obj
    def __call__(self, data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            textblob = self.ensure_dependency("textblob")
            
            text = self.text or data.get(self.text_key, "")
            blob = textblob.TextBlob(text)
            
            polarity = blob.sentiment.polarity
            
            if polarity > 0.3:
                sentiment = "positive"
            elif polarity < -0.3:
                sentiment = "negative"
            else:
                sentiment = "neutral"
            
            data[self.response_key] = {
                "success": True,
                "text": text[:100],  # First 100 chars
                "polarity": polarity,
                "subjectivity": blob.sentiment.subjectivity,
                "sentiment": sentiment
            }
            return data
            
        except Exception as e:
            data[self.response_key] = {"success": False, "error": str(e)}
            raise RuntimeError(f"Sentiment Analysis failed: {str(e)}")
