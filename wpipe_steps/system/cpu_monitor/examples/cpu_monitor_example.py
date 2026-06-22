"""
Example: CpuMonitorStep
Monitor CPU usage before running heavy processes.
"""
from wpipe import Pipeline
from wpipe_steps.system import CpuMonitorStep

def main():
    pipeline = Pipeline(pipeline_name="cpu_monitor_example")
    pipeline.set_steps([
        CpuMonitorStep.as_step(
            name="check_cpu",
            threshold_percent=80.0,
            response_key="cpu_status"
        )
    ])
    result = pipeline.run({})
    print("CPU Status:", result.get("cpu_status"))

if __name__ == "__main__":
    main()
