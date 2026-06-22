from typing import Any, Dict, Optional, List
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep

@step(
    name="sendgrid_email",
    version="v1.0",
    description="Send transactional emails via SendGrid",
    tags=["communication", "sendgrid", "email", "sync"]
)
class SendGridMailStep(BaseStep):
    """
    Step for sending emails using SendGrid API.
    """
    
    def __init__(
        self,
        api_key: str,
        from_email: str,
        to_emails: List[str],
        subject: str,
        content: Optional[str] = None,
        content_key: Optional[str] = None,
        response_key: str = "sendgrid_status",
        name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__(name, version)
        self.api_key = api_key
        self.from_email = from_email
        self.to_emails = to_emails
        self.subject = subject
        self.content = content
        self.content_key = content_key
        self.response_key = response_key

    @to_obj
    def __call__(self, data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            sendgrid = self.ensure_dependency("sendgrid", "sendgrid-python")
            
            from sendgrid.helpers.mail import Mail, Email, Content, To
            
            body = self.content or data.get(self.content_key, "")
            
            mail = Mail(
                from_email=Email(self.from_email),
                to_email=To(self.to_emails[0]),
                subject=self.subject,
                html_content=Content("text/html", body)
            )
            
            for to_email in self.to_emails[1:]:
                mail.add_to(To(to_email))
            
            sg = sendgrid.SendGridAPIClient(api_key=self.api_key)
            response = sg.send(mail)
            
            data[self.response_key] = {
                "success": 200 <= response.status_code < 300,
                "status_code": response.status_code,
                "to": self.to_emails
            }
            return data
            
        except Exception as e:
            data[self.response_key] = {"success": False, "error": str(e)}
            raise RuntimeError(f"SendGrid Mail failed: {str(e)}")
