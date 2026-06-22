import sys
from pathlib import Path

# Add project root to path for local development testing
sys.path.append(str(Path(__file__).parent.parent.parent))

from wpipe import Pipeline
from wpipe_steps.connectivity import OAuth2AuthStep

def main():
    pipeline = Pipeline(pipeline_name="OAuth2_Demo", verbose=True)

    # Note: Execution requires valid client_id/secret and endpoint
    # This is a template of how it would be used
    auth_step = OAuth2AuthStep.as_step(
        name="Auth_Service",
        token_url="https://auth.example.com/oauth/token",
        client_id="my_client_id",
        client_secret="my_secret_key"
    )

    pipeline.set_steps([
        auth_step,
        lambda d: print(f"\n🔑 Token acquired: {d['oauth_token']['access_token'][:10]}...") or d
    ])

    print("🚀 OAuth2 Step defined. (Execution requires real credentials)")

if __name__ == "__main__":
    main()
