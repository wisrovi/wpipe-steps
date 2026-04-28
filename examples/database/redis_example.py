import sys
from pathlib import Path

# Add project root to path for local development testing
sys.path.append(str(Path(__file__).parent.parent.parent))

from wpipe import Pipeline
from wpipe_steps.database import RedisCacheStep

def main():
    pipeline = Pipeline(pipeline_name="Redis_Demo", verbose=True)

    # 1. Set a value
    set_step = RedisCacheStep.as_step(
        name="Cache_User_Session",
        operation="set",
        key="session_123",
        value_key="session_data"
    )

    # 2. Get the value back
    get_step = RedisCacheStep.as_step(
        name="Retrieve_Session",
        operation="get",
        key="session_123",
        response_key="cached_session"
    )

    pipeline.set_steps([
        set_step,
        get_step,
        lambda d: print(f"\n🚀 Cached Data: {d['cached_session']['value']}") or d
    ])

    print("🚀 Redis Steps defined. (Execution requires real server)")

if __name__ == "__main__":
    main()
