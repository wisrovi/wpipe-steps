import sys
from pathlib import Path

# Add project root to path for local development testing
sys.path.append(str(Path(__file__).parent.parent.parent))

from wpipe import Pipeline
from wpipe_steps.database import ClickHouseBulkStep

def print_result(data):
    """Step to print the ClickHouse bulk insert result."""
    status = data.get("clickhouse_status", {})
    if status.get("success"):
        print(f"\n✅ Bulk Insert Successful!")
        print(f"Table: {status['table']}")
        print(f"Records inserted: {status['count']}")
    else:
        print(f"\n❌ Bulk Insert Failed: {status.get('error')}")
    return data

def main():
    # 1. Create the pipeline
    pipeline = Pipeline(pipeline_name="ClickHouse_Bulk_Demo", verbose=True)

    # 2. Define steps
    # Example: Bulk insert records into ClickHouse
    bulk_insert = ClickHouseBulkStep.as_step(
        name="Insert_Analytics_Data",
        host="localhost",
        database="analytics",
        table="events",
        data_key="events_data"
    )

    pipeline.set_steps([
        bulk_insert,
        print_result
    ])

    # 3. Run with sample data
    print("🚀 Starting ClickHouse Bulk Insert Demo Pipeline...")
    sample_data = [
        {"event": "page_view", "user_id": 1, "timestamp": "2024-01-01 10:00:00"},
        {"event": "click", "user_id": 2, "timestamp": "2024-01-01 10:01:00"}
    ]
    pipeline.run({"events_data": sample_data})

if __name__ == "__main__":
    main()
