#!/bin/bash
set -e

echo "Installing requirements..."
pip install pyinstaller rich

echo "Building executable..."
pyinstaller --onefile tsnf_pro.py

echo "Build complete. Executable is located in dist/tsnf_pro"
