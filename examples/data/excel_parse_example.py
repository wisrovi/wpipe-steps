import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))

from wpipe import Pipeline
from wpipe_steps.data import ExcelParseStep

def print_result(data):
    """Step to print Excel parse result."""
    status = data.get("excel_status", {})
    if status.get("success"):
        print(f"\n✅ Excel parsed!")
        print(f"Input: {status['input']}")
        print(f"Rows: {status['rows']}")
        print(f"Data: {data.get('excel_data')[:2]}")  # Show first 2 rows
    else:
        print(f"\n❌ Parse Failed: {status.get('error')}")
    return data

def main():
    pipeline = Pipeline(pipeline_name="Excel_Parse_Demo", verbose=True)

    parse = ExcelParseStep.as_step(
        name="Parse_Excel",
        input_path="test_data.xlsx"
    )

    pipeline.set_steps([
        parse,
        print_result
    ])

    print("🚀 Starting Excel Parse Demo Pipeline...")
    print("Note: Requires a valid .xlsx file to test")
    pipeline.run({})

if __name__ == "__main__":
    main()
