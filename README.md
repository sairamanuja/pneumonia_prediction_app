# Pneumonia Detection Web Application

This web application uses a trained DenseNet model to detect pneumonia from chest X-ray images.

## Features

- Upload chest X-ray images (PNG, JPG, JPEG formats)
- AI-powered pneumonia detection using DenseNet model
- Clean, responsive web interface
- Result display with uploaded image
- File size validation (max 16MB)

## Setup and Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation Steps

1. **Navigate to the project directory:**
   ```bash
   cd /home/sai/Desktop/harsha-ml
   ```

2. **Activate the virtual environment:**
   ```bash
   source .venv/bin/activate
   ```

3. **Install dependencies (if not already installed):**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```

5. **Open your web browser and go to:**
   ```
   http://localhost:5000
   ```

## Usage

1. **Upload Image**: Click "Choose File" and select a chest X-ray image
2. **Get Prediction**: Click "Predict" to analyze the image
3. **View Results**: The application will display whether pneumonia is detected or not
4. **Upload Another**: Click "Upload Another Image" to analyze more images

## File Structure

```
harsha-ml/
├── app.py                          # Main Flask application
├── requirements.txt                # Python dependencies
├── README.md                       # This documentation
├── .gitignore                      # Git ignore rules
├── config/                         # Configuration management
│   ├── __init__.py                # Config module init
│   └── config.py                  # Environment-specific settings
├── models/                         # Machine learning models
│   └── pneumonia_densenet.keras   # Trained DenseNet model
├── templates/                      # HTML templates
│   ├── index.html                 # Upload page
│   └── result.html                # Results page
├── static/                         # Static files
│   └── uploads/                   # User uploaded images
├── docs/                          # Documentation
│   └── structure.md               # Detailed project structure
└── .venv/                         # Python virtual environment
```

## Model Information

- **Model Type**: DenseNet
- **Input Size**: 224x224 pixels
- **Supported Formats**: PNG, JPG, JPEG
- **Output**: Binary classification (NORMAL/PNEUMONIA)

## Troubleshooting

### Common Issues:

1. **Import Errors**: Make sure all dependencies are installed:
   ```bash
   pip install -r requirements.txt
   ```

2. **Model Not Found**: Ensure the model file is in the correct location:
   ```
   models/pneumonia_densenet.keras
   ```

3. **Port Already in Use**: If port 5000 is busy, modify the port in app.py:
   ```python
   app.run(debug=True, host='0.0.0.0', port=5001)  # Change to different port
   ```

4. **File Upload Issues**: Check that the static/uploads directory exists and has write permissions.

## Security Notes

- The application includes file type validation
- File size is limited to 16MB
- Uploaded files are given unique names to prevent conflicts
- Remember to change the secret key in production

## Development

To run in development mode:
```bash
export FLASK_ENV=development
python app.py
```

For production deployment, consider using a WSGI server like Gunicorn.
# pneumonia_prediction_app
