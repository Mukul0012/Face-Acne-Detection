# 🧴 Face Acne Detection & Gut Health Prediction

> An AI-powered web application for detecting facial acne from images using computer vision and providing insights related to skin health.

The project combines **computer vision, deep learning, and a web-based interface** to analyze facial images and identify acne-related conditions.

---

## ✨ Features

* 📸 Upload a facial image for analysis
* 🤖 AI-powered acne detection
* 🔍 Computer vision-based image analysis
* 🧠 Deep learning model using YOLO
* 🌐 Web interface built with Flask
* 📊 Detection results displayed through the web application
* 🖼️ Uploaded images handled through the application's static upload directory
* 🔬 Research-oriented skin and gut-health analysis

---

## 🧠 How It Works

The application follows a simple image-processing and prediction pipeline:

```text
                  ┌─────────────────┐
                  │      User       │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Upload Facial   │
                  │     Image       │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Flask Web       │
                  │ Application     │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Image           │
                  │ Preprocessing   │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ YOLO Detection  │
                  │     Model       │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Acne Detection  │
                  │    Results      │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Display Results │
                  │   to the User   │
                  └─────────────────┘
```

---

# 🛠️ Tech Stack

| Technology     | Purpose                           |
| -------------- | --------------------------------- |
| **Python**     | Core programming language         |
| **Flask**      | Web application backend           |
| **YOLO**       | Object detection / acne detection |
| **PyTorch**    | Deep learning model execution     |
| **HTML/CSS**   | Web interface                     |
| **JavaScript** | Client-side functionality         |
| **OpenCV**     | Image processing                  |
| **Git/GitHub** | Version control                   |

> The trained model is included in the repository as `best.pt`, while the Flask application is implemented in `app.py`.

---

# 📂 Project Structure

```text
Face-Acne-Detection/
│
├── static/
│   └── uploads/
│       └── uploaded images
│
├── templates/
│   └── HTML templates
│
├── app.py
│
├── best.pt
│
├── Face Acne Detection & Gut Health Prediction.pdf
│
├── .gitattributes
│
└── README.md
```

The current repository contains the Flask entry point, YOLO model, templates, upload directory, and project documentation.

---

# 🚀 Getting Started

## Prerequisites

Make sure you have the following installed:

* Python 3.9+
* pip
* Git

For better performance during model inference, a compatible GPU environment can be used, although CPU inference may also be possible depending on the model configuration.

---

## 1. Clone the Repository

```bash
git clone https://github.com/Mukul0012/Face-Acne-Detection.git
```

```bash
cd Face-Acne-Detection
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

Install the required Python packages:

```bash
pip install flask
pip install ultralytics
pip install opencv-python
pip install torch
pip install torchvision
```

If the project contains a `requirements.txt` file in a future version, dependencies can instead be installed with:

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

Start the Flask server:

```bash
python app.py
```

The application will typically be available at:

```text
http://127.0.0.1:5000/
```

Open the URL in your browser and upload a facial image to perform detection.

---

# 🔬 YOLO Model

The repository contains a trained model:

```text
best.pt
```

This model is used by the application for image-based acne detection.

### Detection Pipeline

```text
Input Image
     │
     ▼
Image Preprocessing
     │
     ▼
YOLO Model
     │
     ▼
Object Detection
     │
     ├── Detection Class
     ├── Confidence Score
     └── Bounding Box
     │
     ▼
Detection Result
```

The model allows the application to identify acne-related regions within an uploaded facial image.

---

# 📸 Example Workflow

### Step 1 — Upload Image

The user uploads a facial image through the web interface.

### Step 2 — Image Processing

The Flask backend receives the image and prepares it for model inference.

### Step 3 — AI Detection

The trained YOLO model analyzes the image.

### Step 4 — Display Results

The application returns the detection output to the user.

---

# 🧪 Model Development

The project demonstrates an end-to-end computer vision workflow:

```text
Dataset
   │
   ▼
Image Annotation
   │
   ▼
Data Preparation
   │
   ▼
YOLO Training
   │
   ▼
Model Evaluation
   │
   ▼
best.pt
   │
   ▼
Flask Deployment
```

Important model-development metrics that can be evaluated include:

* Precision
* Recall
* mAP
* IoU
* Confidence score

---

# 📊 Why YOLO?

YOLO (You Only Look Once) is well suited for this type of application because it performs object detection in a single inference pipeline.

For acne detection, this makes it possible to identify multiple acne-related regions within an image while producing:

* Bounding boxes
* Class predictions
* Confidence scores

This approach can provide significantly more useful information than a simple image-level classification model.

---

# 🔐 Privacy & Security Considerations

Because the application processes facial images, privacy should be considered carefully.

Recommended production improvements include:

* Delete uploaded images after processing
* Avoid storing facial images unnecessarily
* Encrypt sensitive data
* Restrict access to uploaded files
* Validate uploaded file types
* Limit maximum upload size
* Prevent arbitrary file execution
* Add HTTPS in production
* Avoid exposing model or server internals

---

# ⚠️ Medical Disclaimer

This project is intended for **educational and research purposes**.

Acne detection results should **not be considered a medical diagnosis**. The application should not be used as a replacement for professional medical or dermatological advice.

Users with persistent, severe, or concerning skin conditions should consult a qualified healthcare professional.

---

# 🔮 Future Improvements

### 🤖 Machine Learning

* [ ] Improve training dataset
* [ ] Increase detection accuracy
* [ ] Add more acne classes
* [ ] Add model evaluation metrics
* [ ] Hyperparameter optimization
* [ ] Data augmentation
* [ ] Model quantization
* [ ] Real-time camera detection

### 🌐 Web Application

* [ ] User authentication
* [ ] User dashboard
* [ ] Detection history
* [ ] Downloadable reports
* [ ] Drag-and-drop image upload
* [ ] Mobile-responsive UI
* [ ] REST API
* [ ] Cloud deployment

### 🔬 Health Analysis

* [ ] Improve gut-health prediction model
* [ ] Integrate additional user inputs
* [ ] Personalized lifestyle recommendations
* [ ] Trend analysis across multiple scans

---

# 🎯 Project Objectives

The primary objectives of this project are to:

* Apply deep learning to a real-world computer vision problem
* Build an end-to-end AI-powered web application
* Understand object detection using YOLO
* Integrate a trained ML model with Flask
* Process and analyze facial images
* Explore the relationship between skin conditions and health-related factors
* Deploy machine learning inference through a web interface

---

# 📚 Learning Outcomes

Through this project, the following concepts are demonstrated:

* Python development
* Flask web development
* Computer vision
* YOLO object detection
* Deep learning
* Image preprocessing
* Model inference
* File uploads
* Web-based ML deployment
* AI application architecture

---

# 🌐 Repository

**GitHub Repository**

https://github.com/Mukul0012/Face-Acne-Detection

---

# 👨‍💻 Author

### Mukul Bhalkar

Computer Engineering Student | AI/ML & Full-Stack Developer

**GitHub:**
https://github.com/Mukul0012

---

# 📄 License

This project is intended primarily for educational and research purposes.

---

## ⭐ Support

If you found this project interesting, consider giving the repository a ⭐ on GitHub.

---

<div align="center">

### Built with 🐍 Python · 🤖 YOLO · 👁️ Computer Vision · 🌐 Flask

</div>
