#!/bin/bash
echo "🚀 Starting Jupyter Lab..."
echo "📖 Notebook will be available at: http://localhost:8888"
echo "🛑 Press Ctrl+C to stop"
jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root
