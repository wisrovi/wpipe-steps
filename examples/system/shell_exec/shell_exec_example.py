import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from wpipe import Pipeline
from wpipe_steps.system.shell_exec import ShellExecStep

def main():
    pipeline = Pipeline(pipeline_name="shell_exec_pipeline")
    pipeline.set_steps([
        ShellExecStep.as_step(name="run_ls", command="echo 'Hello WPipe'")
    ])
    
    result = pipeline.run({})
    print(f"Pipeline Result: {result}")
    
    assert result["shell_status"]["success"] == True
    assert "Hello WPipe" in result["shell_status"]["stdout"]

if __name__ == "__main__":
    main()
