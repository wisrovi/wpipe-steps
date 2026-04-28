import sys
from pathlib import Path

# Add project root to path for local development testing
sys.path.append(str(Path(__file__).parent.parent.parent))

from wpipe import Pipeline
from wpipe_steps.database import ClickHouseBulkStep

def main():
    pipeline = Pipeline(pipeline_name="ClickHouse_Demo", verbose=True)

    # Example: Bulk insert of sensor data
    records = [
        {"sensor_id": 1, "value": 25.5, "timestamp": "2024-01-01 10:00:00"},
        {"sensor_id": 2, "value": 26.1, "timestamp": "2024-01-01 10:01:00"},
    ]

    ch_step = ClickHouseBulkStep.as_step(
        name="Insert_Sensors",
        host="localhost",
        database="analytics",
        table="sensors_history",
        custom_data=records
    )

    pipeline.set_steps([
        ch_step,
        lambda d: print(f"\n📈 ClickHouse Inserted: {d['clickhouse_status']['count']} rows") or d
    ])

    print("🚀 ClickHouse Step defined. (Execution requires real server)")

if __name__ == "__main__":
    main()
