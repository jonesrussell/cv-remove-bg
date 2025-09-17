#!/bin/bash

# Development helper functions
alias ll='ls -la'
alias la='ls -A'
alias l='ls -CF'

# Python helpers
alias py='python'
alias pip='python -m pip'

# Project specific helpers
run-bg-removal() {
    if [ $# -eq 0 ]; then
        python background_removal.py
    else
        python background_removal.py --single "$1"
    fi
}
alias test-env='python test_setup.py'
alias start-jupyter='./start_jupyter.sh'

# Quick commands
alias format-code='black . && isort .'
alias lint-code='flake8 .'
alias test-code='pytest tests/ -v'

echo "🛠️ Development helpers loaded!"
echo "Available commands:"
echo "  run-bg-removal [image]  - Run background removal (all images or single image)"
echo "  test-env               - Test the development environment"
echo "  start-jupyter          - Start Jupyter Lab"
echo "  format-code            - Format code with black and isort"
echo "  lint-code              - Lint code with flake8"
