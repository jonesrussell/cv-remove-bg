#!/usr/bin/env python3
"""
Setup script for the Background Removal with OpenCV project.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="cv-remove-bg",
    version="1.0.0",
    author="CV Background Removal Tool",
    description="A powerful tool for automatically removing backgrounds from images using OpenCV",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Multimedia :: Graphics :: Graphics Conversion",
        "Topic :: Scientific/Engineering :: Image Processing",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "cv-remove-bg=background_removal:main",
        ],
    },
    extras_require={
        "dev": [
            "black>=22.0.0",
            "isort>=5.0.0",
            "flake8>=4.0.0",
            "pytest>=6.0.0",
            "pytest-cov>=3.0.0",
            "pre-commit>=2.15.0",
        ],
        "jupyter": [
            "jupyter>=1.0.0",
            "jupyterlab>=3.0.0",
            "notebook>=6.0.0",
            "ipywidgets>=7.0.0",
            "matplotlib>=3.5.0",
            "seaborn>=0.11.0",
            "pandas>=1.3.0",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
