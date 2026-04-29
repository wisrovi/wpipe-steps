import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from wpipe import Pipeline
from wpipe_steps.system.cpu_monitor import CpuMonitorStep

def main():
    pipeline = Pipeline(pipeline_name="cpu_monitor_pipeline")
    pipeline.set_steps([
        CpuMonitorStep.as_step(name="check_cpu", threshold_percent=80.0)
    ])
    
    result = pipeline.run({})
    print(f"Pipeline Result: {result}")
    
    assert "cpu_status" in result
    assert "cpu_percent" in result["cpu_status"]

if __name__ == "__main__":
    main()
