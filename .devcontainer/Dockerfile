# Use Python 3.11 slim image as base
FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Install system dependencies for OpenCV and other packages
RUN apt-get update && apt-get install -y \
    # OpenCV dependencies
    libopencv-dev \
    python3-opencv \
    # Image processing libraries
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgomp1 \
    # Build tools
    build-essential \
    # Git and other utilities
    git \
    curl \
    wget \
    # Jupyter dependencies
    libfontconfig1 \
    libxrender1 \
    libgl1-mesa-glx \
    # Additional utilities
    vim \
    nano \
    htop \
    tree \
    sudo \
    && rm -rf /var/lib/apt/lists/*

# Create a non-root user
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# Set working directory
WORKDIR /workspaces/cv-remove-bg

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python packages as root first
RUN pip install --upgrade pip \
    && pip install -r requirements.txt \
    && pip install \
        jupyter \
        jupyterlab \
        notebook \
        ipywidgets \
        matplotlib \
        seaborn \
        pandas \
        pillow \
        scikit-image \
        scipy \
        black \
        isort \
        flake8 \
        pytest \
        pytest-cov \
        pre-commit

# Create necessary directories and set permissions
RUN mkdir -p images output \
    && chown -R $USERNAME:$USERNAME /workspaces/cv-remove-bg

# Switch to the non-root user
USER $USERNAME

# Set default shell
SHELL ["/bin/bash", "-c"]

# Expose Jupyter ports
EXPOSE 8888 8889 8890

# Default command
CMD ["bash"]
