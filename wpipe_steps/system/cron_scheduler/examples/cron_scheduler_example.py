"""
Example: CronSchedulerStep
Calculate next execution time based on cron expression.
"""
from wpipe import Pipeline
from wpipe_steps.system import CronSchedulerStep

def main():
    pipeline = Pipeline(pipeline_name="cron_scheduler_example")
    pipeline.set_steps([
        CronSchedulerStep.as_step(
            name="next_run",
            cron_expr="*/15 * * * *",  # Every 15 minutes
            response_key="cron_status"
        )
    ])
    result = pipeline.run({})
    print("Cron Status:", result.get("cron_status"))

if __name__ == "__main__":
    main()
