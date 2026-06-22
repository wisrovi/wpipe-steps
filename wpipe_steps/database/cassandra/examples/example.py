import sys
from pathlib import Path

# Add project root to path for local development testing
sys.path.append(str(Path(__file__).parent.parent.parent))

from wpipe import Pipeline
from wpipe_steps.database import CassandraWriteStep

def print_result(data):
    """Step to print the Cassandra write result."""
    status = data.get("cassandra_status", {})
    if status.get("success"):
        print(f"\n✅ Cassandra Write Successful!")
        print(f"Keyspace: {status['keyspace']}")
        print(f"Table: {status['table']}")
    else:
        print(f"\n❌ Write Failed: {status.get('error')}")
    return data

def main():
    # 1. Create the pipeline
    pipeline = Pipeline(pipeline_name="Cassandra_Write_Demo", verbose=True)

    # 2. Define steps
    # Example: Write a row to Cassandra
    write_row = CassandraWriteStep.as_step(
        name="Write_User_Session",
        contact_points=["127.0.0.1"],
        keyspace="user_sessions",
        table="sessions",
        data_key="session_data"
    )

    pipeline.set_steps([
        write_row,
        print_result
    ])

    # 3. Run with sample data
    print("🚀 Starting Cassandra Write Demo Pipeline...")
    pipeline.run({"session_data": {"session_id": "abc123", "user_id": 1, "created_at": "2024-01-01"}})

if __name__ == "__main__":
    main()
