import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))

from wpipe import Pipeline
from wpipe_steps.multimedia import VideoFrameExtractStep

def print_result(data):
    """Step to print Video Frame Extract result."""
    status = data.get("video_status", {})
    if status.get("success"):
        print(f"\n✅ Frames Extracted!")
        print(f"Output Dir: {status['output_dir']}")
        print(f"Frames: {status['frames_extracted']}")
    else:
        print(f"\n❌ Extraction Failed: {status.get('error')}")
    return data

def main():
    pipeline = Pipeline(pipeline_name="Video_Frame_Demo", verbose=True)

    extract = VideoFrameExtractStep.as_step(
        name="Extract_Frames",
        input_path="test_video.mp4",
        output_dir="frames",
        interval=30
    )

    pipeline.set_steps([
        extract,
        print_result
    ])

    print("🚀 Starting Video Frame Extract Demo Pipeline...")
    print("Note: Requires a valid .mp4 file to test")
    pipeline.run({})

if __name__ == "__main__":
    main()
