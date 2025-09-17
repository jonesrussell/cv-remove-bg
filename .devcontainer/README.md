# Devcontainer Setup for Background Removal with OpenCV

This devcontainer provides a complete development environment for the background removal project with all necessary dependencies pre-installed.

## Features

- 🐍 **Python 3.11** with OpenCV and computer vision libraries
- 📓 **Jupyter Lab/Notebook** support with pre-configured extensions
- 🛠️ **Development Tools**: Black, isort, flake8, pytest
- 🔧 **VS Code Extensions**: Python, Jupyter, GitHub Copilot, and more
- 📁 **Volume Mounts**: Images and output directories are mounted for persistence
- 🚀 **Ready to Run**: All dependencies installed and configured

## Getting Started

### Option 1: VS Code with Dev Containers Extension

1. Install the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) in VS Code
2. Open this project in VS Code
3. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac) and select "Dev Containers: Reopen in Container"
4. Wait for the container to build and start (first time may take a few minutes)

### Option 2: Manual Docker Build

```bash
# Build the container
docker build -f .devcontainer/Dockerfile -t cv-remove-bg .

# Run the container
docker run -it --rm -v $(pwd):/workspaces/cv-remove-bg -p 8888:8888 cv-remove-bg
```

## What's Included

### Python Environment
- Python 3.11
- OpenCV with all dependencies
- NumPy, matplotlib, seaborn, pandas
- Jupyter ecosystem (Lab, Notebook, widgets)
- Development tools (black, isort, flake8, pytest)

### VS Code Extensions
- Python language support with Pylance
- Jupyter notebook support
- Code formatting (Black, isort)
- Linting (flake8)
- GitHub Copilot integration
- JSON, YAML, Markdown support

### Pre-configured Settings
- Auto-formatting on save
- Import organization
- Jupyter notebook integration
- Python path configuration

## Available Commands

Once the container is running, you'll have access to these commands:

```bash
# Run the background removal tool
python background_removal.py

# Process a single image
python background_removal.py --single images/your_image.jpg

# Start Jupyter Lab
jupyter lab --ip=0.0.0.0 --port=8888 --no-browser

# Format code
black . && isort .

# Lint code
flake8 .

# Run tests
pytest tests/ -v
```

## Ports

The following ports are forwarded for easy access:

- **8888**: Jupyter Lab (http://localhost:8888)
- **8889**: Jupyter Notebook (http://localhost:8889)
- **8890**: Custom applications

## Directory Structure

```
/workspaces/cv-remove-bg/
├── images/                    # Input images (mounted from host)
├── output/                    # Output images (mounted from host)
├── background_removal.py      # Main script
├── background_removal.ipynb   # Jupyter notebook
├── requirements.txt           # Python dependencies
└── .devcontainer/            # Devcontainer configuration
```

## Development Workflow

1. **Add images** to the `images/` directory on your host machine
2. **Open the project** in VS Code with the devcontainer
3. **Run the tool** using the command line or Jupyter notebook
4. **Check results** in the `output/` directory
5. **Modify code** with full IDE support and live reloading

## Troubleshooting

### Container Won't Start
- Ensure Docker is running
- Check that the Dockerfile is valid
- Try rebuilding the container: `Dev Containers: Rebuild Container`

### Python Import Errors
- Run `pip install -r requirements.txt` to reinstall dependencies
- Check that you're using the correct Python interpreter (should be in the container)

### Jupyter Not Accessible
- Ensure port 8888 is forwarded
- Check the container logs for any errors
- Try accessing http://localhost:8888 in your browser

### Permission Issues
- The container runs as a non-root user (`vscode`)
- Files created in the container should have correct permissions
- If you encounter permission issues, check the file ownership

## Customization

### Adding New Dependencies
1. Add packages to `requirements.txt`
2. Rebuild the container: `Dev Containers: Rebuild Container`

### Modifying VS Code Settings
Edit `.devcontainer/devcontainer.json` and update the `settings` section.

### Adding New Extensions
Add extension IDs to the `extensions` array in `devcontainer.json`.

## Performance Notes

- The container includes OpenCV with system dependencies for optimal performance
- Volume mounts ensure your data persists between container restarts
- The container is optimized for development with fast startup times

## Support

If you encounter any issues with the devcontainer setup:

1. Check the container logs in VS Code
2. Verify all required files are present
3. Try rebuilding the container
4. Check the [Dev Containers documentation](https://code.visualstudio.com/docs/remote/containers)

---

Happy coding! 🚀
