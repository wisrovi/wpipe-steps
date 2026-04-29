import os
import re
import tomli
import tomli_w
import subprocess
import time

STATES_TO_ADD = [
    {
        "name": "CpuMonitorStep",
        "filename": "cpu_monitor",
        "description": "Obtener carga del sistema antes de procesos pesados.",
        "deps": ["psutil"],
        "code": '''from typing import Any, Dict, Optional
from wpipe_steps.core.base import BaseStep

class CpuMonitorStep(BaseStep):
    """
    Step for monitoring CPU usage.
    """
    def __init__(self, name: Optional[str] = None, version: str = "v1.0", threshold_percent: float = 90.0, response_key: str = "cpu_status"):
        super().__init__(name, version)
        self.threshold_percent = threshold_percent
        self.response_key = response_key

    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        psutil = self.ensure_dependency("psutil")
        
        cpu_percent = psutil.cpu_percent(interval=1)
        is_overloaded = cpu_percent >= self.threshold_percent
        
        data[self.response_key] = {
            "cpu_percent": cpu_percent,
            "is_overloaded": is_overloaded,
            "threshold": self.threshold_percent
        }
        
        return data
''',
        "example": '''import sys
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
'''
    },
    {
        "name": "ShellExecStep",
        "filename": "shell_exec",
        "description": "Ejecución controlada de comandos Bash/PowerShell.",
        "deps": [],
        "code": '''from typing import Any, Dict, Optional
import subprocess
from wpipe_steps.core.base import BaseStep

class ShellExecStep(BaseStep):
    """
    Step for executing shell commands.
    """
    def __init__(self, command: str, name: Optional[str] = None, version: str = "v1.0", response_key: str = "shell_status"):
        super().__init__(name, version)
        self.command = command
        self.response_key = response_key

    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            result = subprocess.run(self.command, shell=True, capture_output=True, text=True, check=True)
            data[self.response_key] = {
                "success": True,
                "stdout": result.stdout.strip(),
                "stderr": result.stderr.strip(),
                "returncode": result.returncode
            }
        except subprocess.CalledProcessError as e:
            data[self.response_key] = {
                "success": False,
                "stdout": e.stdout.strip(),
                "stderr": e.stderr.strip(),
                "returncode": e.returncode,
                "error": str(e)
            }
        
        return data
''',
        "example": '''import sys
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
'''
    },
    {
        "name": "DiskSpaceCheckStep",
        "filename": "disk_space_check",
        "description": "Alerta si queda poco espacio para el proceso.",
        "deps": ["psutil"],
        "code": '''from typing import Any, Dict, Optional
import shutil
from wpipe_steps.core.base import BaseStep

class DiskSpaceCheckStep(BaseStep):
    """
    Step for checking disk space.
    """
    def __init__(self, path: str = "/", name: Optional[str] = None, version: str = "v1.0", response_key: str = "disk_status", min_free_gb: float = 1.0):
        super().__init__(name, version)
        self.path = path
        self.response_key = response_key
        self.min_free_gb = min_free_gb

    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        total, used, free = shutil.disk_usage(self.path)
        free_gb = free / (2**30)
        
        data[self.response_key] = {
            "path": self.path,
            "total_gb": total / (2**30),
            "used_gb": used / (2**30),
            "free_gb": free_gb,
            "has_enough_space": free_gb >= self.min_free_gb
        }
        
        return data
''',
        "example": '''import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from wpipe import Pipeline
from wpipe_steps.system.disk_space_check import DiskSpaceCheckStep

def main():
    pipeline = Pipeline(pipeline_name="disk_space_pipeline")
    pipeline.set_steps([
        DiskSpaceCheckStep.as_step(name="check_disk", path=".", min_free_gb=0.1)
    ])
    
    result = pipeline.run({})
    print(f"Pipeline Result: {result}")
    
    assert "disk_status" in result
    assert "free_gb" in result["disk_status"]

if __name__ == "__main__":
    main()
'''
    },
    {
        "name": "HealthCheckStep",
        "filename": "health_check",
        "description": "Ping a una lista de servicios críticos.",
        "deps": ["requests"],
        "code": '''from typing import Any, Dict, List, Optional
from wpipe_steps.core.base import BaseStep

class HealthCheckStep(BaseStep):
    """
    Step for checking health of HTTP services.
    """
    def __init__(self, urls: List[str], name: Optional[str] = None, version: str = "v1.0", response_key: str = "health_status"):
        super().__init__(name, version)
        self.urls = urls
        self.response_key = response_key

    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        requests = self.ensure_dependency("requests")
        
        status = {}
        all_healthy = True
        
        for url in self.urls:
            try:
                response = requests.get(url, timeout=5)
                is_ok = response.ok
                status[url] = {"up": is_ok, "status_code": response.status_code}
                if not is_ok:
                    all_healthy = False
            except Exception as e:
                status[url] = {"up": False, "error": str(e)}
                all_healthy = False
                
        data[self.response_key] = {
            "all_healthy": all_healthy,
            "services": status
        }
        
        return data
''',
        "example": '''import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from wpipe import Pipeline
from wpipe_steps.system.health_check import HealthCheckStep

def main():
    pipeline = Pipeline(pipeline_name="health_check_pipeline")
    pipeline.set_steps([
        HealthCheckStep.as_step(name="ping_services", urls=["https://httpbin.org/get", "https://status.io"])
    ])
    
    result = pipeline.run({})
    print(f"Pipeline Result: {result}")
    
    assert "health_status" in result
    assert "all_healthy" in result["health_status"]

if __name__ == "__main__":
    main()
'''
    },
    {
        "name": "CronSchedulerStep",
        "filename": "cron_scheduler",
        "description": "Programar la siguiente ejecución del pipeline.",
        "deps": ["croniter"],
        "code": '''from typing import Any, Dict, Optional
from datetime import datetime
from wpipe_steps.core.base import BaseStep

class CronSchedulerStep(BaseStep):
    """
    Step for calculating next execution time based on a cron expression.
    """
    def __init__(self, cron_expr: str, name: Optional[str] = None, version: str = "v1.0", response_key: str = "cron_status"):
        super().__init__(name, version)
        self.cron_expr = cron_expr
        self.response_key = response_key

    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        croniter = self.ensure_dependency("croniter")
        
        now = datetime.now()
        cron = croniter.croniter(self.cron_expr, now)
        next_run = cron.get_next(datetime)
        
        data[self.response_key] = {
            "cron_expression": self.cron_expr,
            "current_time": now.isoformat(),
            "next_execution": next_run.isoformat()
        }
        
        return data
''',
        "example": '''import sys
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
'''
    }
]

def run_cmd(cmd):
    print(f"Running: {cmd}")
    subprocess.run(cmd, shell=True, check=True)

def update_version(increment="minor"):
    with open("pyproject.toml", "rb") as f:
        config = tomli.load(f)
    
    v = config["project"]["version"].split(".")
    if increment == "minor":
        new_v = f"{v[0]}.{int(v[1])+1}.0"
    else:
        new_v = f"{v[0]}.{v[1]}.{int(v[2])+1}"
        
    config["project"]["version"] = new_v
    
    with open("pyproject.toml", "wb") as f:
        tomli_w.dump(config, f)
        
    init_path = "wpipe_steps/__init__.py"
    if os.path.exists(init_path):
        with open(init_path, "r") as f:
            content = f.read()
        content = re.sub(r'__version__ = ".*"', f'__version__ = "{new_v}"', content)
        with open(init_path, "w") as f:
            f.write(content)
            
    return new_v

def main():
    # Make sure folders exist
    os.makedirs("wpipe_steps/system", exist_ok=True)
    os.makedirs("examples/system", exist_ok=True)
    
    for state in STATES_TO_ADD:
        print(f"\
--- Processing {state['name']} ---")
        
        # 1. Install deps if any to run example
        if state["deps"]:
            run_cmd(f"pip install {' '.join(state['deps'])}")
            
        # 2. Write code
        step_path = f"wpipe_steps/system/{state['filename']}.py"
        with open(step_path, "w") as f:
            f.write(state["code"])
            
        # 3. Write example
        example_dir = f"examples/system/{state['filename']}"
        os.makedirs(example_dir, exist_ok=True)
        example_path = f"{example_dir}/{state['filename']}_example.py"
        with open(example_path, "w") as f:
            f.write(state["example"])
            
        req_path = f"{example_dir}/requirements.txt"
        with open(req_path, "w") as f:
            f.write("\
".join(state["deps"]) + "\
" if state["deps"] else "wpipe\
")
            
        readme_path = f"{example_dir}/README.md"
        with open(readme_path, "w") as f:
            f.write(f"# Example for {state['name']}\
\
Run `python {state['filename']}_example.py`")

        # 4. Update __init__.py in wpipe_steps/system
        system_init = "wpipe_steps/system/__init__.py"
        if not os.path.exists(system_init):
            with open(system_init, "w") as f:
                f.write(f"from .{state['filename']} import {state['name']}\
")
        else:
            with open(system_init, "a") as f:
                f.write(f"from .{state['filename']} import {state['name']}\
")

        # 5. Test example
        print("Testing example...")
        run_cmd(f"python {example_path}")
        
        # 6. Update TODO.txt
        with open("TODO.txt", "r") as f:
            todo = f.read()
        todo = todo.replace(f"    {state['name']}: {state['description']}", f"    ✅ {state['name']}: {state['description']}")
        if "⚙️ 9. Sistema y Utilidades" in todo and not "✅ COMPLETADO" in todo and "HealthCheckStep" == state["name"]:
            # If all are done (simulated by last step), mark pack as completed
            pass 
        with open("TODO.txt", "w") as f:
            f.write(todo)

        # 7. Update README.md (Append to a system section or just modify if exists)
        # We will dynamically inject the new state into the README.md or just append for now
        with open("README.md", "r") as f:
            readme = f.read()
            
        if "### System (package: `wpipe_steps.system`)" not in readme:
            system_section = "\
\
### System (package: `wpipe_steps.system`)\
| Step Name | Import | Type | Example | Description |\
|-----------|--------|------|---------|-------------|\
"
            readme = readme + system_section
            
        new_row = f"| `{state['filename']}` | `from wpipe_steps.system import {state['name']}` | Sync | [{state['filename']}_example.py]({example_path}) | {state['description']} |\
"
        readme += new_row
        
        with open("README.md", "w") as f:
            f.write(readme)

        # 8. Bump Version
        new_version = update_version(increment="minor")
        print(f"Bumped version to {new_version}")

        # 9. Build Sphinx Docs
        print("Building Sphinx docs...")
        run_cmd("sphinx-apidoc -f -o docs/source/api wpipe_steps/")
        run_cmd("cd docs && make html")

        # 10. Commit changes
        print("Committing changes...")
        run_cmd("git add .")
        run_cmd(f'git commit -m "[FEATURE] Add {state["name"]} and update version to {new_version}"')

        # 11. Publish to PyPI (simulated or executed)
        print("Publishing to PyPI...")
        run_cmd("python setup.py sdist bdist_wheel")
        try:
            # TWINE_USERNAME and TWINE_PASSWORD are required for twine upload.
            # We'll use `--skip-existing` and just run it. If it fails (due to lack of auth), it's fine, we catch it.
            # Usually users have TWINE_USERNAME set or .pypirc, we'll try to run it.
            run_cmd("twine upload dist/* --skip-existing")
        except subprocess.CalledProcessError:
            print("Warning: twine upload failed, likely due to missing credentials. Continuing since git commit is done.")

    print("All 5 states generated successfully!")

if __name__ == "__main__":
    main()
