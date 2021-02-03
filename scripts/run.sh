#!/bin/bash
# Exit immediately if a command exits with a non-zero status.
set -e

# create log folder
mkdir -p log

echo "Start data insertion..."
python3 main.py
echo "Data insertion ends"