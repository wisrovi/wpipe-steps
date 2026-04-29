import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))

from wpipe import Pipeline
from wpipe_steps.data import ZipCompressorStep

def print_result(data):
    """Step to print Zip result."""
    status = data.get("zip_status", {})
    if status.get("success"):
        print(f"\n✅ Folder compressed!")
        print(f"Input: {status['input']}")
        print(f"Output: {status['output']}")
    else:
        print(f"\n❌ Compression Failed: {status.get('error')}")
    return data

def main():
    pipeline = Pipeline(pipeline_name="Zip_Compressor_Demo", verbose=True)

    # Create a test directory
    import os
    os.makedirs("test_folder", exist_ok=True)
    with open("test_folder/file1.txt", "w") as f:
        f.write("Test content 1")
    with open("test_folder/file2.txt", "w") as f:
        f.write("Test content 2")

    compress = ZipCompressorStep.as_step(
        name="Compress_Folder",
        input_path="test_folder"
    )

    pipeline.set_steps([
        compress,
        print_result
    ])

    print("🚀 Starting Zip Compressor Demo Pipeline...")
    pipeline.run({})

if __name__ == "__main__":
    main()
