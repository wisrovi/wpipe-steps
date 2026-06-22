import sys
from pathlib import Path

# Add project root to path for local development testing
sys.path.append(str(Path(__file__).parent.parent.parent))

from wpipe import Pipeline
from wpipe_steps.database import MongoInsertStep

def print_result(data):
    """Step to print the MongoDB insert result."""
    status = data.get("mongo_status", {})
    if status.get("success"):
        print(f"\n✅ Insert Successful!")
        print(f"Inserted IDs: {status['inserted_ids']}")
    else:
        print(f"\n❌ Insert Failed: {status.get('error')}")
    return data

def main():
    # 1. Create the pipeline
    pipeline = Pipeline(pipeline_name="Mongo_Insert_Demo", verbose=True)

    # 2. Define steps
    # Example: Insert a document into MongoDB
    insert_doc = MongoInsertStep.as_step(
        name="Insert_User_Document",
        uri="mongodb://localhost:27017",
        database="test_db",
        collection="users",
        document_key="user_data"
    )

    pipeline.set_steps([
        insert_doc,
        print_result
    ])

    # 3. Run with sample data
    print("🚀 Starting MongoDB Insert Demo Pipeline...")
    pipeline.run({"user_data": {"name": "John Doe", "email": "john@example.com"}})

if __name__ == "__main__":
    main()
