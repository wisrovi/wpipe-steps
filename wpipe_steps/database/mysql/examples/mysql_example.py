import sys
from pathlib import Path

# Add project root to path for local development testing
sys.path.append(str(Path(__file__).parent.parent.parent))

from wpipe import Pipeline
from wpipe_steps.database import MySQLQueryStep

def main():
    pipeline = Pipeline(pipeline_name="MySQL_Demo", verbose=True)

    # Example: Select from a users table
    db_step = MySQLQueryStep.as_step(
        name="Get_DB_Users",
        host="localhost",
        user="admin",
        password="secret_password",
        database="production_db",
        query="SELECT id, username FROM users WHERE active = %s",
        params=(1,)
    )

    pipeline.set_steps([
        db_step,
        lambda d: print(f"\n📊 DB Results: {d['mysql_results']['data']}") or d
    ])

    print("🚀 MySQL Step defined. (Execution requires real database)")

if __name__ == "__main__":
    main()
