import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from wpipe import Pipeline
from wpipe_steps.system.health_check import HealthCheckStep

def main():
    pipeline = Pipeline(pipeline_name="health_check_pipeline")
    pipeline.set_steps([
        HealthCheckStep.as_step(name="ping_services", urls=["https://httpbin.org/get"])
    ])
    
    result = pipeline.run({})
    print(f"Pipeline Result: {result}")
    
    assert "health_status" in result
    assert "all_healthy" in result["health_status"]

if __name__ == "__main__":
    main()
