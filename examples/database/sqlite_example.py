import sys
import os
from pathlib import Path

# Add project root to path for local development testing
sys.path.append(str(Path(__file__).parent.parent.parent))

from wpipe import Pipeline
from wpipe_steps.database import SQLiteAuditStep

def main():
    pipeline = Pipeline(pipeline_name="SQLite_Audit_Demo", verbose=True)

    db_path = "test_audit.db"
    
    # Cleanup old test db
    if os.path.exists(db_path):
        os.remove(db_path)

    # Example: Audit current state
    audit_step = SQLiteAuditStep.as_step(
        name="Local_Audit",
        db_path=db_path,
        data_keys=["user", "action"]
    )

    pipeline.set_steps([
        audit_step,
        lambda d: print(f"\n📁 SQLite Audit saved to {d['audit_status']['db_path']}") or d
    ])

    print("🚀 Running SQLite Audit Demo...")
    pipeline.run({"user": "wisrovi", "action": "testing_steps"})

if __name__ == "__main__":
    main()
