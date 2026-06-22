import sys
from pathlib import Path

# Add project root to path for local development testing
sys.path.append(str(Path(__file__).parent.parent.parent))

from wpipe import Pipeline
from wpipe_steps.database import MongoInsertStep

def main():
    pipeline = Pipeline(pipeline_name="MongoDB_Demo", verbose=True)

    # Example: Insert a telemetry log
    log_step = MongoInsertStep.as_step(
        name="Log_to_Mongo",
        uri="mongodb://admin:secret@localhost:27017",
        database="logs_db",
        collection="telemetry",
        custom_document={"event": "system_check", "status": "ok", "version": "1.0"}
    )

    pipeline.set_steps([
        log_step,
        lambda d: print(f"\n🍃 Mongo Insert Status: {d['mongo_status']['success']} (ID: {d['mongo_status']['inserted_ids']})") or d
    ])

    print("🚀 MongoDB Step defined. (Execution requires real server)")

if __name__ == "__main__":
    main()
