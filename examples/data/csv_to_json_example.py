import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))

from wpipe import Pipeline
from wpipe_steps.data import CsvToJsonStep

def print_result(data):
    """Step to print CSV to JSON result."""
    status = data.get("csv_json_status", {})
    if status.get("success"):
        print(f"\n✅ CSV converted to JSON!")
        print(f"Input: {status['input']}")
        print(f"Output: {status['output']}")
        print(f"Rows: {status['rows']}")
    else:
        print(f"\n❌ Conversion Failed: {status.get('error')}")
    return data

def main():
    pipeline = Pipeline(pipeline_name="CSV_to_JSON_Demo", verbose=True)

    # Create a sample CSV for testing
    with open("test_data.csv", "w") as f:
        f.write("name,age,city\nJohn,30,NYC\nJane,25,LA\n")

    convert = CsvToJsonStep.as_step(
        name="Convert_CSV",
        input_path="test_data.csv"
    )

    pipeline.set_steps([
        convert,
        print_result
    ])

    print("🚀 Starting CSV to JSON Demo Pipeline...")
    pipeline.run({})

if __name__ == "__main__":
    main()
