#!/bin/bash

# Post-creation setup script for devcontainer
echo "🚀 Setting up Background Removal development environment..."

# Ensure we're in the right directory
cd /workspaces/cv-remove-bg

# Create necessary directories if they don't exist
mkdir -p images output

# Install the package in development mode if setup.py exists
if [ -f "setup.py" ]; then
    echo "📦 Installing package in development mode..."
    pip install -e .
fi

# Configure Jupyter
echo "⚙️ Configuring Jupyter..."
jupyter lab --generate-config
mkdir -p ~/.jupyter

# Create Jupyter config to allow external access
cat > ~/.jupyter/jupyter_lab_config.py << EOF
c.ServerApp.ip = '0.0.0.0'
c.ServerApp.port = 8888
c.ServerApp.open_browser = False
c.ServerApp.allow_root = True
c.ServerApp.token = ''
c.ServerApp.password = ''
c.ServerApp.notebook_dir = '/workspaces/cv-remove-bg'
EOF

# Install system dependencies for OpenGL (fallback)
echo "🔧 Installing OpenGL system dependencies..."
sudo apt-get update && sudo apt-get install -y \
    libgl1-mesa-glx \
    libgl1-mesa-dri \
    libx11-6 \
    libgthread-2.0-0 \
    libgtk-3-0 \
    libgdk-pixbuf2.0-0 \
    libxss1 \
    libgconf-2-4 \
    && sudo rm -rf /var/lib/apt/lists/*

# Install OpenCV and other dependencies
echo "📦 Installing OpenCV and dependencies..."
pip install opencv-python-headless numpy tqdm matplotlib seaborn pandas pillow scikit-image scipy

# Install Jupyter extensions
echo "📓 Installing Jupyter extensions..."
pip install jupyter jupyterlab notebook ipywidgets

# Create a simple test script
cat > test_setup.py << 'EOF'
#!/usr/bin/env python3
"""Test script to verify the development environment is working."""

import sys
import cv2
import numpy as np
from pathlib import Path

def test_environment():
    """Test that all required packages are installed and working."""
    print("🧪 Testing development environment...")
    
    # Test OpenCV
    try:
        print(f"✅ OpenCV version: {cv2.__version__}")
    except Exception as e:
        print(f"❌ OpenCV error: {e}")
        return False
    
    # Test NumPy
    try:
        test_array = np.array([1, 2, 3])
        print(f"✅ NumPy working: {test_array.sum()}")
    except Exception as e:
        print(f"❌ NumPy error: {e}")
        return False
    
    # Test project structure
    required_dirs = ['images', 'output']
    for dir_name in required_dirs:
        if Path(dir_name).exists():
            print(f"✅ Directory exists: {dir_name}")
        else:
            print(f"❌ Missing directory: {dir_name}")
            return False
    
    print("🎉 Development environment is ready!")
    return True

if __name__ == "__main__":
    success = test_environment()
    sys.exit(0 if success else 1)
EOF

# Run the test
echo "🔍 Running environment test..."
python test_setup.py

# Create a helpful startup script
cat > start_jupyter.sh << 'EOF'
#!/bin/bash
echo "🚀 Starting Jupyter Lab..."
echo "📖 Notebook will be available at: http://localhost:8888"
echo "🛑 Press Ctrl+C to stop"
jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root
EOF

chmod +x start_jupyter.sh

# Create a development helper script
cat > dev_helpers.sh << 'EOF'
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
EOF

chmod +x dev_helpers.sh

# Add to bashrc
echo "source /workspaces/cv-remove-bg/dev_helpers.sh" >> ~/.bashrc

echo "✅ Devcontainer setup complete!"
echo ""
echo "🎯 Quick start commands:"
echo "  python background_removal.py              # Run background removal"
echo "  ./start_jupyter.sh                       # Start Jupyter Lab"
echo "  python test_setup.py                     # Test environment"
echo ""
echo "📖 Jupyter Lab will be available at http://localhost:8888"
echo "🔧 VS Code extensions for Python and Jupyter are pre-installed"
