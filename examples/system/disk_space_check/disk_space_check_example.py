import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from wpipe import Pipeline
from wpipe_steps.system.disk_space_check import DiskSpaceCheckStep

def main():
    pipeline = Pipeline(pipeline_name="disk_space_pipeline")
    pipeline.set_steps([
        DiskSpaceCheckStep.as_step(name="check_disk", path=".", min_free_gb=0.1)
    ])
    
    result = pipeline.run({})
    print(f"Pipeline Result: {result}")
    
    assert "disk_status" in result
    assert "free_gb" in result["disk_status"]

if __name__ == "__main__":
    main()
