"""
Example: DiskSpaceCheckStep
Check disk space before processing large files.
"""
from wpipe import Pipeline
from wpipe_steps.system import DiskSpaceCheckStep

def main():
    pipeline = Pipeline(pipeline_name="disk_space_example")
    pipeline.set_steps([
        DiskSpaceCheckStep.as_step(
            name="check_disk",
            path="/",
            min_free_gb=5.0,
            response_key="disk_status"
        )
    ])
    result = pipeline.run({})
    print("Disk Status:", result.get("disk_status"))

if __name__ == "__main__":
    main()
