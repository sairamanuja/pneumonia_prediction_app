from flask import Flask, request, render_template, url_for, flash, redirect
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os
from werkzeug.utils import secure_filename
import uuid
from config.config import config

# Initialize Flask app
app = Flask(__name__)

# Load configuration
env = os.environ.get('FLASK_ENV', 'development')
app.config.from_object(config[env])

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Load the trained model
try:
    model = load_model(app.config['MODEL_PATH'])
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

def allowed_file(filename):
    """Check if the uploaded file has an allowed extension"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def predict_pneumonia(img_path):
    """Predict pneumonia from chest X-ray image"""
    try:
        # Load and preprocess the image
        img = image.load_img(img_path, target_size=(224, 224))
        img_array = image.img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)
        
        # Make prediction
        prediction = model.predict(img_array)
        
        # Return prediction result
        return "PNEUMONIA" if prediction[0][0] > 0.5 else "NORMAL"
    except Exception as e:
        print(f"Error during prediction: {e}")
        return "ERROR"

@app.route("/", methods=["GET"])
def index():
    """Home page with upload form"""
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    """Handle file upload and prediction"""
    if model is None:
        flash("Model not loaded. Please check the model file.", "error")
        return render_template("index.html", error="Model not available")
    
    # Check if file is in request
    if 'file' not in request.files:
        flash("No file selected", "error")
        return render_template("index.html", error="Please select a file")
    
    file = request.files['file']
    
    # Check if file is selected
    if file.filename == '':
        flash("No file selected", "error")
        return render_template("index.html", error="Please select a file")
    
    # Check if file is allowed
    if not allowed_file(file.filename):
        flash("Invalid file type. Please upload PNG, JPG, or JPEG files only.", "error")
        return render_template("index.html", error="Invalid file type. Please upload PNG, JPG, or JPEG files only.")
    
    try:
        # Secure the filename and add unique identifier
        filename = secure_filename(file.filename)
        unique_filename = f"{uuid.uuid4().hex}_{filename}"
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        
        # Save the file
        file.save(file_path)
        
        # Make prediction
        prediction_result = predict_pneumonia(file_path)
        
        if prediction_result == "ERROR":
            flash("Error processing the image. Please try again.", "error")
            return render_template("index.html", error="Error processing the image")
        
        # Render result page
        return render_template("result.html", 
                             prediction=prediction_result, 
                             filename=unique_filename)
    
    except Exception as e:
        flash(f"An error occurred: {str(e)}", "error")
        return render_template("index.html", error="An error occurred while processing your request")

@app.errorhandler(413)
def too_large(e):
    """Handle file too large error"""
    return render_template("index.html", error="File too large. Please upload an image smaller than 16MB."), 413

if __name__ == "__main__":
    # Create upload directory if it doesn't exist
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    
    print("Starting Pneumonia Detection App...")
    print(f"Open your browser and go to http://localhost:{app.config['PORT']}")
    
    app.run(debug=app.config['DEBUG'], 
            host=app.config['HOST'], 
            port=app.config['PORT'])
