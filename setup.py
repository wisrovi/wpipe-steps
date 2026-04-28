from pathlib import Path
from setuptools import setup, find_packages

# Read README for long description
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text() if (this_directory / "README.md").exists() else ""

# Read requirements
requirements_file = this_directory / "requirements.txt"
requirements = []
if requirements_file.exists():
    with open(requirements_file, "r") as f:
        requirements = [line.strip() for line in f if line.strip() and not line.startswith("#")]

setup(
    name="wpipe-steps",
    version="0.8.0",
    packages=find_packages(include=["wpipe_steps", "wpipe_steps.*"]),
    install_requires=requirements or [
        "wpipe>=2.3.0",
        "requests>=2.31.0",
        "pydantic>=2.0.0",
        "paramiko>=3.0.0",
        "feedparser>=6.0.0",
        "pymysql>=1.1.0",
    ],
        "feedparser>=6.0.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    description="A professional collection of pre-built steps and states for the WPipe orchestration engine.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wisrovi/wpipe-steps",
    author="William Steve Rodriguez Villamizar",
    author_email="wisrovi.rodriguez@gmail.com",
    license="MIT",
    python_requires=">=3.9",
)
