"""
Example: HealthCheckStep
Monitor health of critical HTTP services.
"""
from wpipe import Pipeline
from wpipe_steps.system import HealthCheckStep

def main():
    pipeline = Pipeline(pipeline_name="health_check_example")
    pipeline.set_steps([
        HealthCheckStep.as_step(
            name="check_services",
            urls=["https://httpbin.org/status/200", "https://httpbin.org/status/500"],
            response_key="health_status"
        )
    ])
    result = pipeline.run({})
    print("Health Status:", result.get("health_status"))

if __name__ == "__main__":
    main()
