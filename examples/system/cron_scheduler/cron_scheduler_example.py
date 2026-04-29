import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from wpipe import Pipeline
from wpipe_steps.system.cron_scheduler import CronSchedulerStep

def main():
    pipeline = Pipeline(pipeline_name="cron_pipeline")
    pipeline.set_steps([
        CronSchedulerStep.as_step(name="calculate_next_run", cron_expr="0 12 * * *")
    ])
    
    result = pipeline.run({})
    print(f"Pipeline Result: {result}")
    
    assert "cron_status" in result
    assert "next_execution" in result["cron_status"]

if __name__ == "__main__":
    main()
