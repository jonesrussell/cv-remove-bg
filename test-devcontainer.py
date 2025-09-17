#!/usr/bin/env python3
"""
Quick test script to verify the devcontainer environment is working.
Run this after the devcontainer starts up.
"""

import sys
import subprocess
from pathlib import Path

def test_environment():
    """Test the devcontainer environment."""
    print("🧪 Testing devcontainer environment...")
    print("=" * 50)
    
    # Test Python version
    print(f"✅ Python version: {sys.version}")
    
    # Test required packages
    required_packages = [
        'cv2', 'numpy', 'tqdm', 'matplotlib', 
        'seaborn', 'pandas', 'PIL', 'skimage', 'scipy'
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package} - OK")
        except ImportError:
            print(f"❌ {package} - MISSING")
            missing_packages.append(package)
    
    # Test project structure
    required_dirs = ['images', 'output']
    for dir_name in required_dirs:
        if Path(dir_name).exists():
            print(f"✅ Directory: {dir_name}")
        else:
            print(f"❌ Missing directory: {dir_name}")
    
    # Test background removal script
    if Path('background_removal.py').exists():
        print("✅ background_removal.py - Found")
    else:
        print("❌ background_removal.py - Missing")
    
    # Test Jupyter
    try:
        result = subprocess.run(['jupyter', '--version'], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print("✅ Jupyter - OK")
        else:
            print("❌ Jupyter - Not working")
    except Exception as e:
        print(f"❌ Jupyter - Error: {e}")
    
    # Summary
    print("\n" + "=" * 50)
    if missing_packages:
        print(f"❌ Missing packages: {', '.join(missing_packages)}")
        print("Run: pip install " + " ".join(missing_packages))
        return False
    else:
        print("🎉 Devcontainer environment is ready!")
        print("\nQuick commands:")
        print("  python background_removal.py              # Run background removal")
        print("  jupyter lab --ip=0.0.0.0 --port=8888     # Start Jupyter Lab")
        print("  python test-devcontainer.py               # Run this test")
        return True

if __name__ == "__main__":
    success = test_environment()
    sys.exit(0 if success else 1)
