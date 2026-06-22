#!/bin/bash
# Run wpipe-steps unit tests inside a Docker container using docker run

# Get the directory of this script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PARENT_DIR="$(dirname "$DIR")"

echo "🐳 Running unit tests in python:3.10-slim container..."

# Execute the test suite using pytest inside the container
docker run --rm \
  -v "$PARENT_DIR:/workspace" \
  -w /workspace/wpipe-steps \
  python:3.10-slim bash -c "
    pip install --upgrade pip && \
    pip install -e /workspace/wpipe && \
    pip install -e . && \
    pip install pytest pytest-cov && \
    pytest --cov=wpipe_steps --cov-report=term-missing tests/
  "
