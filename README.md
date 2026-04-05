# Diabetic Retinopathy Detection System
# Overview

This project is an AI-based system designed to detect and classify Diabetic Retinopathy, a serious eye disease caused by diabetes that can lead to vision loss if not diagnosed early.

The model uses Machine Learning / Deep Learning techniques to analyze retinal images and patient health data to predict the stage of the disease and associated risk level.

# What is Diabetic Retinopathy?

Diabetic Retinopathy is a diabetes-related eye condition that affects the blood vessels in the retina. Early detection is crucial to prevent permanent vision damage.

# Features
🔍 Detects diabetic retinopathy from retinal images
📊 Predicts disease stage (No DR, Mild, Moderate, Severe, Proliferative)
🧬 Uses patient health metrics (age, BP, glucose, BMI, etc.)
🤖 AI/ML-based prediction model
🌐 Simple web interface for user input
⚡ Fast and accurate prediction system
# Technologies Used
Python 🐍
TensorFlow / Keras (Deep Learning) OR Scikit-learn (ML)
OpenCV (Image Processing)
NumPy & Pandas (Data Handling)
Flask (Web Framework)
HTML, CSS, JavaScript (Frontend)

# How It Works
User uploads retinal image and/or health data
Image is preprocessed (resizing, normalization, enhancement)
Model extracts features from retina image
AI model predicts disease stage
Result is displayed with risk level
# How to Run
-- Clone repository
git clone https://github.com/your-username/diabetic-retinopathy.git

-- Move into project folder
cd diabetic-retinopathy

-- Install dependencies
pip install -r requirements.txt

-- Run Flask app
python app.py
