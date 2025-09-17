#!/bin/bash

# Development helper functions
alias ll='ls -la'
alias la='ls -A'
alias l='ls -CF'

# Python helpers
alias py='python'
alias pip='python -m pip'

# Project specific helpers
alias run-bg-removal='python background_removal.py'
alias test-env='python test_setup.py'
alias start-jupyter='./start_jupyter.sh'

# Quick commands
alias format-code='black . && isort .'
alias lint-code='flake8 .'
alias test-code='pytest tests/ -v'

echo "🛠️ Development helpers loaded!"
echo "Available commands:"
echo "  run-bg-removal  - Run the background removal tool"
echo "  test-env        - Test the development environment"
echo "  start-jupyter   - Start Jupyter Lab"
echo "  format-code     - Format code with black and isort"
echo "  lint-code       - Lint code with flake8"
