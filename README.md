# Background Removal with OpenCV

A powerful tool for automatically removing backgrounds from images using OpenCV's GrabCut algorithm. Perfect for batch processing images with clear foreground/background separation.

## Features

- 🚀 **Batch Processing**: Process multiple images at once
- 🎯 **Automatic Background Removal**: Uses OpenCV's GrabCut algorithm
- 🖼️ **Transparent PNG Output**: Preserves transparency for easy compositing
- 📊 **Progress Tracking**: Real-time progress bars and detailed logging
- 🛠️ **Command Line Interface**: Easy-to-use CLI with multiple options
- 📓 **Jupyter Notebook**: Interactive notebook for experimentation

## Installation

### Option 1: Devcontainer (Recommended)

The easiest way to get started is using the included devcontainer setup:

1. **Install Prerequisites**:
   - [Docker Desktop](https://www.docker.com/products/docker-desktop/)
   - [Cursor](https://cursor.sh/)
   - [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

2. **Open in Devcontainer**:
   - Clone this repository
   - Open in Cursor
   - Press `Ctrl+Shift+P` → "Dev Containers: Reopen in Container"
   - Wait for the container to build (first time: ~2-3 minutes)

3. **Test the Setup**:
   ```bash
   python test_setup.py
   ```

4. **You're Ready!** All dependencies are pre-installed and configured.

#### What's Pre-installed

**Python Packages:**
- `opencv-python-headless` - Computer vision library
- `numpy` - Numerical computing
- `tqdm` - Progress bars
- `jupyter` - Interactive notebooks
- `matplotlib` - Plotting library
- `seaborn` - Statistical visualization
- `pandas` - Data manipulation

**Development Tools:**
- `black` - Code formatting
- `isort` - Import sorting
- `flake8` - Code linting
- `pytest` - Testing framework

**Cursor Extensions:**
- Python language support
- Jupyter notebook integration
- GitHub Copilot
- JSON, YAML, Markdown support
- Git integration

#### Available Commands

**In the Container Terminal:**
```bash
# Run background removal on all images
python background_removal.py

# Process a single image
python background_removal.py --single images/sample_circle.jpg

# Start Jupyter Lab
jupyter lab --ip=0.0.0.0 --port=8888 --no-browser

# Format code
black . && isort .

# Lint code
flake8 .
```

**Cursor Tasks (Ctrl+Shift+P → "Tasks: Run Task"):**
- **Run Background Removal** - Process all images
- **Format Code** - Auto-format with black and isort
- **Lint Code** - Check code quality with flake8
- **Start Jupyter Lab** - Launch Jupyter in background

**Cursor Debug Configurations (F5):**
- **Background Removal - All Images**
- **Background Removal - Single Image**
- **Background Removal - Custom Margin**
- **Background Removal - Custom Directories**

#### Access Points
- **Jupyter Lab**: http://localhost:8888
- **Jupyter Notebook**: http://localhost:8889
- **Custom Port**: http://localhost:8890

### Option 2: Local Installation

1. Clone or download this repository
2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Quick Start

### Using the Command Line Script

1. **Place your images** in the `images/` folder (supports JPG, JPEG, PNG, BMP, TIFF)
2. **Run the script**:
   ```bash
   python background_removal.py
   ```
3. **Check results** in the `output/` folder

### Using the Jupyter Notebook

1. Start Jupyter Lab or Jupyter Notebook
2. Open `background_removal.ipynb`
3. Run all cells to process your images
4. View results with built-in visualization

## Usage Examples

### Basic Usage
```bash
# Process all images in the default 'images/' folder
python background_removal.py
```

### Advanced Options
```bash
# Process a single image
python background_removal.py --single path/to/image.jpg

# Custom input/output directories
python background_removal.py --input my_images --output results

# Adjust GrabCut margin (default: 5%)
python background_removal.py --margin 0.1

# Verbose logging
python background_removal.py --verbose
```

### Command Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `--input`, `-i` | Input directory containing images | `images` |
| `--output`, `-o` | Output directory for processed images | `output` |
| `--single`, `-s` | Process a single image file | None |
| `--margin`, `-m` | Margin percentage for GrabCut rectangle | `0.05` (5%) |
| `--verbose`, `-v` | Enable verbose logging | False |

## Success Indicators

Your devcontainer is working when you see:
- ✅ Container starts without errors
- ✅ Cursor connects successfully
- ✅ `python test_setup.py` passes all tests
- ✅ `import cv2` works in Python
- ✅ Jupyter Lab accessible at localhost:8888

## Project Structure

```
cv-remove-bg/
├── images/                    # Input images (jpg, jpeg, png, bmp, tiff)
├── output/                    # Processed images with transparent backgrounds
├── background_removal.py      # Command-line script
├── background_removal.ipynb   # Jupyter notebook
├── test_setup.py             # Environment test script
├── requirements.txt           # Python dependencies
├── pyproject.toml             # Modern Python package configuration
├── .devcontainer/            # Devcontainer configuration
│   ├── devcontainer.json     # Devcontainer settings
│   └── postCreateCommand.sh  # Post-creation setup script
├── .gitignore                # Git ignore rules
└── README.md                 # This file
```

## How It Works

The tool uses OpenCV's **GrabCut algorithm** to automatically separate foreground objects from backgrounds:

1. **Image Analysis**: Reads input images and calculates optimal processing rectangle
2. **GrabCut Segmentation**: Applies the GrabCut algorithm with a 5% margin
3. **Mask Generation**: Creates binary masks distinguishing foreground from background
4. **Transparency Application**: Converts images to RGBA format with transparent backgrounds
5. **Output**: Saves processed images as PNG files with preserved transparency

## Tips for Best Results

### Image Preparation
- ✅ Use high-quality images with clear contrast
- ✅ Center your subject in the frame
- ✅ Ensure well-lit subjects with distinct shadows
- ✅ Simple, uniform backgrounds work best

### What Works Well
- Portrait photos with plain backgrounds
- Product shots on white/colored backgrounds
- Objects with clear edges and contrast
- Images with minimal background clutter

### Limitations
- ❌ Complex, textured backgrounds
- ❌ Subjects that blend into background
- ❌ Images with poor lighting or low contrast
- ❌ Very small or highly detailed subjects

## Customization

### Adding New Dependencies
1. Add to `requirements.txt`
2. Rebuild container: `Dev Containers: Rebuild Container`

### Modifying Cursor Settings
Edit `.devcontainer/devcontainer.json` → `customizations.vscode.settings`

### Adding Extensions
Edit `.devcontainer/devcontainer.json` → `customizations.vscode.extensions`

## Development Workflow

1. **Open Project** → Cursor with devcontainer
2. **Add Images** → Place in `images/` directory
3. **Run Tool** → Use command line or Jupyter notebook
4. **Check Results** → View in `output/` directory
5. **Modify Code** → Full IDE support with live reloading

## Advanced Usage

### Programmatic Usage

```python
from background_removal import BackgroundRemover

# Initialize remover
remover = BackgroundRemover(
    input_dir="my_images",
    output_dir="results", 
    margin=0.1  # 10% margin
)

# Process all images
remover.process_all_images()

# Process single image
remover.process_single_image("path/to/image.jpg")
```

### Customizing the Algorithm

You can modify the GrabCut parameters in the code:

```python
# In process_image function, adjust these parameters:
cv2.grabCut(img, mask, rect, bgd_model, fgd_model, 
            5,  # Number of iterations (default: 5)
            cv2.GC_INIT_WITH_RECT)  # Initialization method
```

## Troubleshooting

### Devcontainer Issues

**If the container won't build:**

1. **Clear Docker cache**:
   ```bash
   docker system prune -a
   ```

2. **Try manual Docker setup**:
   ```bash
   # Pull the base image
   docker pull mcr.microsoft.com/devcontainers/python:3.11
   
   # Run manually
   docker run -it --rm -v $(pwd):/workspaces/cv-remove-bg -p 8888:8888 mcr.microsoft.com/devcontainers/python:3.11
   ```

**If you get OpenCV import errors:**

```bash
# Install system dependencies
sudo apt-get update
sudo apt-get install -y libgl1-mesa-glx libgl1-mesa-dri libx11-6

# Install OpenCV
pip install opencv-python-headless
```

**Container Won't Start:**
- Ensure Docker Desktop is running
- Try `Dev Containers: Rebuild Container`
- Check Docker logs for errors

**Port Access Issues:**
- Verify ports 8888-8890 are forwarded
- Check container is running: `docker ps`
- Try accessing http://localhost:8888

**Python Import Errors:**
- Run `pip install -r requirements.txt` to reinstall
- Check Python interpreter: `which python`
- Verify virtual environment activation

### Common Issues

**"No valid image files found"**
- Ensure images are in supported formats (jpg, jpeg, png, bmp, tiff)
- Check that images are in the correct input directory

**Poor segmentation results**
- Try adjusting the margin parameter (`--margin 0.1`)
- Use images with better contrast between subject and background
- Ensure subjects are well-lit and clearly defined

**Memory issues with large images**
- Resize images before processing
- Process images in smaller batches

### Error Messages

- `FileNotFoundError`: Input directory doesn't exist
- `Skipping [filename] (unable to read)`: Corrupted or unsupported image file
- `Error processing [filename]`: General processing error (check image format)

## Performance Notes

- **Processing Time**: Typically 1-3 seconds per image depending on size and complexity
- **Memory Usage**: Moderate memory usage, suitable for batch processing
- **Output Size**: PNG files with transparency are typically larger than original JPEGs

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve this tool!

## License

This project is open source and available under the MIT License.

## Next Steps

For even better results, consider integrating with:

- **Deep Learning Models**: U-2-Net, MODNet, MediaPipe Selfie Segmentation
- **Manual Refinement Tools**: Interactive mask editing
- **Background Replacement**: Add custom backgrounds or blur effects
- **Web Interface**: Streamlit or Gradio for easy web-based usage

## Additional Resources

- [Dev Containers Documentation](https://code.visualstudio.com/docs/remote/containers)
- [OpenCV Python Tutorials](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)
- [Jupyter Lab Documentation](https://jupyterlab.readthedocs.io/)

---

**Happy background removing!** 🎨✨
