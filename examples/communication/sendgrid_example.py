import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))

from wpipe import Pipeline
from wpipe_steps.communication import SendGridMailStep

def print_result(data):
    """Step to print SendGrid result."""
    status = data.get("sendgrid_status", {})
    if status.get("success"):
        print(f"\n✅ Email Sent!")
        print(f"Status Code: {status['status_code']}")
    else:
        print(f"\n❌ SendGrid Failed: {status.get('error')}")
    return data

def main():
    pipeline = Pipeline(pipeline_name="SendGrid_Demo", verbose=True)

    # Replace with your actual SendGrid API key
    send_email = SendGridMailStep.as_step(
        name="Send_Email",
        api_key="YOUR_SENDGRID_API_KEY",
        from_email="sender@example.com",
        to_emails=["recipient@example.com"],
        subject="Pipeline Notification",
        content="<h1>Pipeline completed successfully!</h1>"
    )

    pipeline.set_steps([
        send_email,
        print_result
    ])

    print("🚀 Starting SendGrid Mail Demo Pipeline...")
    pipeline.run({})

if __name__ == "__main__":
    main()
