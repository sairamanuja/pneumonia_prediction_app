# Project Structure

This document outlines the organized structure of the Pneumonia Detection Web Application.

## Directory Structure

```
harsha-ml/
├── app.py                          # Main Flask application
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
├── config/                         # Configuration files
│   ├── __init__.py                # Config module init
│   └── config.py                  # Application configuration
├── models/                         # ML model files
│   └── pneumonia_densenet.keras   # Trained DenseNet model
├── templates/                      # HTML templates
│   ├── index.html                 # Upload page template
│   └── result.html                # Results page template
├── static/                         # Static files
│   └── uploads/                   # Directory for uploaded images
├── docs/                          # Documentation
│   └── structure.md               # This file
└── .venv/                         # Python virtual environment
```

## File Descriptions

### Core Application Files
- **app.py**: Main Flask application with routes and business logic
- **requirements.txt**: Lists all Python package dependencies
- **README.md**: Main project documentation with setup instructions

### Configuration
- **config/config.py**: Contains environment-specific configurations
- **config/__init__.py**: Makes config a Python module

### Machine Learning
- **models/pneumonia_densenet.keras**: Pre-trained DenseNet model for pneumonia detection

### Web Interface
- **templates/index.html**: Upload form with responsive design
- **templates/result.html**: Results display page with image preview
- **static/uploads/**: Directory where uploaded images are stored

### Documentation
- **docs/structure.md**: This project structure documentation

### Environment
- **.venv/**: Python virtual environment containing all dependencies

## Key Features of the Organized Structure

1. **Separation of Concerns**: Configuration, models, templates, and documentation are in separate directories
2. **Scalability**: Easy to add new models, templates, or configuration environments
3. **Maintainability**: Clear organization makes the codebase easy to navigate and modify
4. **Security**: Upload directory is properly organized within static files
5. **Environment Management**: Dedicated virtual environment for dependency isolation

## Configuration Management

The application uses environment-based configuration:
- **Development**: Debug mode enabled, runs on localhost:5000
- **Production**: Debug disabled, configurable port via environment variables

## Model Management

Models are stored in the dedicated `models/` directory, making it easy to:
- Version different model files
- Switch between models
- Add new trained models

## Template Organization

HTML templates are organized in the `templates/` directory following Flask conventions:
- Reusable template structure
- Consistent styling
- Easy to extend with new pages
