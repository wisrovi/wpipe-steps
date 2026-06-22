#!/bin/bash
# Calculate code coverage of wpipe-steps project using pytest-cov

# Ensure local wpipe is on PYTHONPATH
export PYTHONPATH=$(pwd)/../wpipe:$PYTHONPATH

# Run pytest with coverage report
pytest --cov=wpipe_steps --cov-report=term-missing tests/
