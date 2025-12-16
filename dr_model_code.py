import numpy as np
import cv2

# ================= IMAGE PREPROCESSING =================
def preprocess_image(img_path):
    img = cv2.imread(img_path)

    if img is None:
        raise ValueError(f"Image not found: {img_path}")

    img = cv2.resize(img, (224, 224))
    img = img / 255.0
    return img

# ================= STAGES =================
stages_list = ['No DR', 'Mild', 'Moderate', 'Severe', 'Proliferative']

# ================= RISK LOGIC =================
def calculate_stage(clinical):
    age, bp, glucose, bmi, hba1c, tg, micro, fh, alcohol, smoking, eye = clinical

    score = 0
    if glucose > 200: score += 2
    if hba1c > 8: score += 2
    if micro > 30: score += 2
    if bp > 140: score += 1
    if smoking == 1: score += 1
    if alcohol == 1: score += 1

    if score <= 1:
        return 'No DR'
    elif score <= 3:
        return 'Mild'
    elif score <= 5:
        return 'Moderate'
    elif score <= 7:
        return 'Severe'
    else:
        return 'Proliferative'

def calculate_risk(stage):
    if stage in ['No DR', 'Mild']:
        return 'Low Risk'
    elif stage == 'Moderate':
        return 'Medium Risk'
    else:
        return 'High Risk'

def safety_precautions(stage):
    return {
        'No DR': 'Healthy diet, exercise, annual eye screening.',
        'Mild': 'Strict glucose control, yearly retinal exam.',
        'Moderate': 'Ophthalmologist consultation, regular monitoring.',
        'Severe': 'Immediate specialist care, laser therapy may be required.',
        'Proliferative': 'Urgent treatment, injections or surgery needed.'
    }[stage]

# ================= FINAL PREDICTION =================
def predict_retinopathy(image_path, clinical_data):
    _ = preprocess_image(image_path)  # validates image
    stage = calculate_stage(clinical_data)
    risk = calculate_risk(stage)
    precautions = safety_precautions(stage)
    return stage, risk, precautions
