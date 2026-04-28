import sys
import os
from pathlib import Path

# Add project root to path for local development testing
sys.path.append(str(Path(__file__).parent.parent))

from wpipe import Pipeline
from wpipe_steps.core.base import BaseStep

# 1. Define a custom step inheriting from BaseStep
class LoggerStep(BaseStep):
    """A simple step that logs data and adds a timestamp."""
    def execute(self, data):
        import datetime
        print(f"[LoggerStep] Processing data at {datetime.datetime.now()}")
        data["log_status"] = "Processed by LoggerStep"
        return data

# 2. Create the pipeline
pipeline = Pipeline(pipeline_name="Example_WPipe_Steps", verbose=True)

# 3. Add steps using the .as_step() factory method
pipeline.set_steps([
    LoggerStep.as_step(name="initial_log", version="v1.1"),
    # Here you would normally use pre-built steps like:
    # HttpRequestStep.as_step(url="https://api.test.com"),
])

# 4. Run it
if __name__ == "__main__":
    print("🚀 Running WPipe-Steps Example...")
    result = pipeline.run({"user": "wisrovi"})
    print(f"\n✅ Result: {result}")
