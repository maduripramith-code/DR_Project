import cv2
import numpy as np

def predict_retinopathy(image_path, clinical_data):
    img = cv2.imread(image_path)
    if img is None:
        return "Error", "Error", "Image not found"

    img = cv2.resize(img, (224,224))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    edge_score = cv2.Canny(gray, 50, 150).mean()

    glucose = clinical_data[2]
    hba1c = clinical_data[4]

    score = (edge_score / 100) + (glucose / 200) + (hba1c * 0.5)

    if score < 2:
        stage = "No DR"
    elif score < 3:
        stage = "Mild"
    elif score < 4:
        stage = "Moderate"
    elif score < 5:
        stage = "Severe"
    else:
        stage = "Proliferative"

    risk = "Low Risk" if stage in ["No DR", "Mild"] else "High Risk"

    precautions = {
        "No DR": "Maintain healthy lifestyle and annual eye screening.",
        "Mild": "Control blood sugar and yearly retinal exam.",
        "Moderate": "Consult ophthalmologist and manage diabetes.",
        "Severe": "Immediate specialist treatment required.",
        "Proliferative": "Urgent surgical or laser intervention needed."
    }

    return stage, risk, precautions[stage]
