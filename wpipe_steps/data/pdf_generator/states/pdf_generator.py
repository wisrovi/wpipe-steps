from typing import Any, Dict, Optional
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep

@step(
    name="pdf_generator",
    version="v1.0",
    description="Create PDF reports from templates",
    tags=["data", "pdf", "sync"]
)
class PdfGeneratorStep(BaseStep):
    """
    Step for generating PDF reports.
    Requires 'reportlab' library.
    """
    
    def __init__(
        self,
        content: Optional[Dict[str, Any]] = None,
        content_key: Optional[str] = None,
        output_path: str = "report.pdf",
        response_key: str = "pdf_status",
        name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__(name, version)
        self.content = content
        self.content_key = content_key
        self.output_path = output_path
        self.response_key = response_key

    @to_obj
    def __call__(self, data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            reportlab = self.ensure_dependency("reportlab", "reportlab")
            from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
            from reportlab.lib.styles import getSampleStyleSheet
            
            content = self.content or data.get(self.content_key, {})
            
            doc = SimpleDocTemplate(self.output_path)
            styles = getSampleStyleSheet()
            story = []
            
            for key, value in content.items():
                story.append(Paragraph(f"<b>{key}:</b> {value}", styles["Normal"]))
                story.append(Spacer(1, 12))
            
            doc.build(story)
            
            data[self.response_key] = {
                "success": True,
                "output": self.output_path
            }
            return data
            
        except Exception as e:
            data[self.response_key] = {"success": False, "error": str(e)}
            raise RuntimeError(f"PDF Generator failed: {str(e)}")
