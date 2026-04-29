import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))

from wpipe import Pipeline
from wpipe_steps.multimedia import ImageResizerStep

def print_result(data):
    """Step to print Image Resizer result."""
    status = data.get("image_status", {})
    if status.get("success"):
        print(f"\n✅ Image Resized!")
        print(f"Output: {status['output']}")
        print(f"Size: {status['size']}")
    else:
        print(f"\n❌ Resize Failed: {status.get('error')}")
    return data

def main():
    pipeline = Pipeline(pipeline_name="Image_Resizer_Demo", verbose=True)

    resize = ImageResizerStep.as_step(
        name="Resize_Image",
        input_path="test_image.jpg",
        width=800
    )

    pipeline.set_steps([
        resize,
        print_result
    ])

    print("🚀 Starting Image Resizer Demo Pipeline...")
    print("Note: Requires a valid .jpg file to test")
    pipeline.run({})

if __name__ == "__main__":
    main()
