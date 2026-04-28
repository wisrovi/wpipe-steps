import sys
from pathlib import Path

# Add project root to path for local development testing
sys.path.append(str(Path(__file__).parent.parent.parent))

from wpipe import Pipeline
from wpipe_steps.database import SQLiteAuditStep

def print_result(data):
    """Step to print the SQLite audit result."""
    status = data.get("audit_status", {})
    if status.get("success"):
        print(f"\n✅ Audit Logged!")
        print(f"DB Path: {status['db_path']}")
        print(f"Audit ID: {status['audit_id']}")
    else:
        print(f"\n❌ Audit Failed: {status.get('error')}")
    return data

def main():
    # 1. Create the pipeline
    pipeline = Pipeline(pipeline_name="SQLite_Audit_Demo", verbose=True)

    # 2. Define steps
    # Example: Audit log an action
    audit_log = SQLiteAuditStep.as_step(
        name="Log_User_Action",
        db_path="audit.db",
        table_name="audit_logs",
        data_keys=["action", "user_id"]
    )

    pipeline.set_steps([
        audit_log,
        print_result
    ])

    # 3. Run with sample data
    print("🚀 Starting SQLite Audit Demo Pipeline...")
    pipeline.run({"action": "user_login", "user_id": 12345})

if __name__ == "__main__":
    main()
