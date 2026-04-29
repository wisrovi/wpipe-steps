"""
Example: ShellExecStep
Execute shell commands safely within a pipeline.
"""
from wpipe import Pipeline
from wpipe_steps.system import ShellExecStep

def main():
    pipeline = Pipeline(pipeline_name="shell_exec_example")
    pipeline.set_steps([
        ShellExecStep.as_step(
            name="list_files",
            command="ls -la",
            response_key="shell_output"
        )
    ])
    result = pipeline.run({})
    print("Shell Output:", result.get("shell_output"))

if __name__ == "__main__":
    main()
