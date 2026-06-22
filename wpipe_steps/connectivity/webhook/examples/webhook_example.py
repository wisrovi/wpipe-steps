import sys
from pathlib import Path

# Add project root to path for local development testing
sys.path.append(str(Path(__file__).parent.parent.parent))

from wpipe import Pipeline
from wpipe_steps.connectivity import WebhookTriggerStep

def main():
    pipeline = Pipeline(pipeline_name="Webhook_Demo", verbose=True)

    # Example using Webhook.site or similar mock service
    # In a real scenario, this would be your Discord/Slack/Custom API webhook
    notify_external = WebhookTriggerStep.as_step(
        name="External_Notification",
        webhook_url="https://webhook.site/546c7662-8e14-41d3-8f0a-6c17f46617a2", # Change this for testing
        custom_payload={"event": "pipeline_started", "priority": "high"},
        response_key="notify_status"
    )

    pipeline.set_steps([
        notify_external,
        lambda d: print(f"\n🔔 Webhook Sent: {d['notify_status']['success']}") or d
    ])

    pipeline.run({"task": "deployment"})

if __name__ == "__main__":
    main()
