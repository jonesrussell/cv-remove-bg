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
