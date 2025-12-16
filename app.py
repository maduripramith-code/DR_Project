from flask import Flask, render_template, request
import os
from dr_model_code import predict_retinopathy

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    stage = risk = precautions = None

    if request.method == "POST":
        image = request.files.get("image")
        if image:
            image_path = os.path.join(UPLOAD_FOLDER, image.filename)
            image.save(image_path)

            clinical_data = [
                int(request.form["age"]),
                float(request.form["bp"]),
                float(request.form["glucose"]),
                float(request.form["bmi"]),
                float(request.form["hba1c"]),
                float(request.form["triglycerides"]),
                float(request.form["microalbuminuria"]),
                int(request.form["family_history"]),
                int(request.form["alcohol"]),
                int(request.form["smoking"]),
                int(request.form["eye_side"])
            ]

            stage, risk, precautions = predict_retinopathy(image_path, clinical_data)

    return render_template(
        "index.html",
        stage=stage,
        risk=risk,
        precautions=precautions
    )

if __name__ == "__main__":
    app.run()
