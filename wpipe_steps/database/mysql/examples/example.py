import sys
from pathlib import Path

# Add project root to path for local development testing
sys.path.append(str(Path(__file__).parent.parent.parent))

from wpipe import Pipeline
from wpipe_steps.database import MySQLQueryStep

def print_result(data):
    """Step to print the MySQL query result."""
    results = data.get("mysql_results", {})
    if results.get("success"):
        print(f"\n✅ Query Successful!")
        print(f"Results: {results['data']}")
    else:
        print(f"\n❌ Query Failed: {results.get('error')}")
    return data

def main():
    # 1. Create the pipeline
    pipeline = Pipeline(pipeline_name="MySQL_Query_Demo", verbose=True)

    # 2. Define steps
    # Example: Select users from a MySQL database
    query_users = MySQLQueryStep.as_step(
        name="Get_All_Users",
        host="localhost",
        user="root",
        password="password",
        database="test_db",
        query="SELECT * FROM users LIMIT 10",
        fetch_results=True
    )

    pipeline.set_steps([
        query_users,
        print_result
    ])

    # 3. Run
    print("🚀 Starting MySQL Query Demo Pipeline...")
    pipeline.run({})

if __name__ == "__main__":
    main()
