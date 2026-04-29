import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))

from wpipe import Pipeline
from wpipe_steps.communication import TwilioSmsStep

def print_result(data):
    """Step to print Twilio result."""
    status = data.get("twilio_status", {})
    if status.get("success"):
        print(f"\n✅ SMS Sent!")
        print(f"Message SID: {status['message_sid']}")
    else:
        print(f"\n❌ Twilio Failed: {status.get('error')}")
    return data

def main():
    pipeline = Pipeline(pipeline_name="Twilio_Demo", verbose=True)

    # Replace with your actual Twilio credentials
    send_sms = TwilioSmsStep.as_step(
        name="Send_SMS",
        account_sid="YOUR_ACCOUNT_SID",
        auth_token="YOUR_AUTH_TOKEN",
        from_number="+1234567890",
        to_number="+0987654321",
        message="🚀 Pipeline alert: Process completed!"
    )

    pipeline.set_steps([
        send_sms,
        print_result
    ])

    print("🚀 Starting Twilio SMS Demo Pipeline...")
    pipeline.run({})

if __name__ == "__main__":
    main()
