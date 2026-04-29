import os
from pathlib import Path
from setuptools import setup, find_packages

# Read README for long description
this_directory = Path(__file__).parent
long_description = (
    (this_directory / "README.md").read_text()
    if (this_directory / "README.md").exists()
    else ""
)

setup(
    name="wpipe-steps",
    version="0.50.0",
    packages=find_packages(include=["wpipe_steps", "wpipe_steps.*"]),
    install_requires=[
        "wpipe>=1.0.0",
        "pydantic>=2.0.0",
        "requests>=2.31.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    description="A professional collection of pre-built steps and states for the wpipe orchestration engine. Lightweight and modular.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wisrovi/wpipe-steps",
    author="William Steve Rodriguez Villamizar",
    author_email="wisrovi.rodriguez@gmail.com",
    license="MIT",
    python_requires=">=3.9",
)
