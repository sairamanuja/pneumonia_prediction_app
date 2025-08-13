#!/bin/bash
# Start script for Pneumonia Detection App

echo "Starting Pneumonia Detection Application..."

# Activate virtual environment
source .venv/bin/activate

# Set environment
export FLASK_ENV=development

# Run the application
python app.py
