import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))

from wpipe import Pipeline
from wpipe_steps.infrastructure import DockerContainerStep

def print_result(data):
    """Step to print the Docker operation result."""
    status = data.get("docker_status", {})
    if status.get("success"):
        print(f"\n✅ Operation Successful!")
        print(f"Container: {status['container']}")
        print(f"Action: {status['action']} - {status['status']}")
    else:
        print(f"\n❌ Operation Failed: {status.get('error')}")
    return data

def main():
    pipeline = Pipeline(pipeline_name="Docker_Container_Demo", verbose=True)

    manage_container = DockerContainerStep.as_step(
        name="Start_Container",
        container_name="my-web-app",
        action="start"
    )

    pipeline.set_steps([
        manage_container,
        print_result
    ])

    print("🚀 Starting Docker Container Demo Pipeline...")
    pipeline.run({})

if __name__ == "__main__":
    main()
