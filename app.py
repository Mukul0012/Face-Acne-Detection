import os
import cv2
import numpy as np
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from ultralytics import YOLO
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import pandas as pd  # Make sure to import pandas

# Initialize Flask app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Load YOLOv8 model
MODEL_PATH = 'runs/detect/train7/weights/best.pt'  # Update with your correct model path
model = YOLO("best.pt")

# Simulated gut health data
gut_health_factors = ["Microbiome Diversity", "Sugar Intake", "Probiotic Levels", "Inflammation Markers", "Stress Levels"]

# Train a mock classifier (this part should ideally use real gut health data)
scaler = StandardScaler()
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)

# Mock training data for gut health (simulated)
X_mock = np.random.rand(100, len(gut_health_factors))  # Random data for 100 samples
y_mock = np.random.choice([0, 1], size=100)  # 0 = Healthy, 1 = Acne Present
X_scaled = scaler.fit_transform(X_mock)
rf_model.fit(X_scaled, y_mock)

# Function to classify acne location
def classify_acne_location(x1, y1, x2, y2, img_shape):
    h, w, _ = img_shape
    face_center_x = w // 2
    if y1 < h * 0.3:
        return "Forehead"
    elif y1 > h * 0.7:
        return "Chin"
    elif x1 < face_center_x and x2 < face_center_x:
        return "Left Cheek"
    elif x1 > face_center_x and x2 > face_center_x:
        return "Right Cheek"
    else:
        return "Nose"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files['image']
        if not file:
            return render_template("index.html", error="No file selected.")

        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        image = cv2.imread(filepath)
        results = model.predict(image)

        acne_locations = set()

        for result in results:
            for box in result.boxes.xyxy:
                x1, y1, x2, y2 = map(int, box)
                location = classify_acne_location(x1, y1, x2, y2, image.shape)
                acne_locations.add(location)
                cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(image, location, (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        # Save output image
        output_path = os.path.join(app.config['UPLOAD_FOLDER'], f"output_{filename}")
        cv2.imwrite(output_path, image)

        # Simulate gut health data for the new sample (based on the defined factors)
        gut_health_data = np.random.rand(1, len(gut_health_factors))  # Simulate a new sample
        gut_health_values = dict(zip(gut_health_factors, gut_health_data[0]))  # Map values to gut health factors

        # Normalize and predict gut health
        scaled_sample = scaler.transform(gut_health_data)
        gut_prediction = rf_model.predict(scaled_sample)[0]
        gut_label = "Likely Healthy Gut" if gut_prediction == 0 else "Potential Gut Imbalance"

        # Convert the simulated data into a DataFrame to display it in tabular format
        gut_health_df = pd.DataFrame([gut_health_values])

        return render_template("index.html",
                               uploaded_img_path=output_path,
                               acne_info=list(acne_locations),
                               gut_pred=gut_label,
                               gut_health_values=gut_health_df.to_html(classes='table table-bordered', index=False))

    return render_template("index.html")

if __name__ == "__main__":
    os.makedirs("static/uploads", exist_ok=True)
    app.run(debug=True)
