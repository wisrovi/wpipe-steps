import sys
from pathlib import Path

# Add project root to path for local development testing
sys.path.append(str(Path(__file__).parent.parent.parent))

from wpipe import Pipeline
from wpipe_steps.database import CassandraWriteStep

def main():
    pipeline = Pipeline(pipeline_name="Cassandra_Demo", verbose=True)

    # Example: Insert a user record
    cassandra_step = CassandraWriteStep.as_step(
        name="Save_User_Cassandra",
        contact_points=["127.0.0.1"],
        keyspace="users_ks",
        table="profiles",
        data_key="user_profile"
    )

    pipeline.set_steps([
        cassandra_step,
        lambda d: print(f"\n⚡ Cassandra Write Success: {d['cassandra_status']['success']}") or d
    ])

    print("🚀 Cassandra Step defined. (Execution requires real cluster)")

if __name__ == "__main__":
    main()
