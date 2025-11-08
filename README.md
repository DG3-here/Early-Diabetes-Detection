# 🩺 Early Diabetes Detection – Machine Learning Health Prediction System

An interactive **machine learning-powered health prediction platform** that detects early signs of **diabetes** based on medical parameters.  
Designed with a **frosted glass UI** (Apple-style), it provides users with **instant health predictions**, along with **personalized diet, exercise, and precautionary suggestions** based on risk level.

---

## 🚀 Features

- 🧠 **ML-based Prediction:** Uses Logistic Regression to analyze multiple health metrics.  
- 🌐 **Interactive Web Interface:** Built using Flask + Bootstrap with a modern glassmorphism UI.  
- 🧾 **Detailed Health Report:** Displays risk level with tailored diet, fitness, and precaution tips.  
- 💾 **Data-Driven Model:** Trained on the PIMA Diabetes dataset for high accuracy.  
- 📊 **Clean Visualization:** Input ranges for metrics like glucose, BMI, and blood pressure.  
- 🔒 **Offline Model:** Works completely locally—no API keys required.

---

## 🧩 Tech Stack

| Layer | Technology Used |
|-------|------------------|
| **Frontend** | HTML5, CSS3, Bootstrap 5 |
| **Backend** | Flask (Python) |
| **Machine Learning** | Scikit-learn, Pandas, NumPy |
| **Model Storage** | Pickle (.pkl) |
| **Dataset** | PIMA Indians Diabetes Dataset (Kaggle) |

---

## 📂 Project Structure
<pre>
Early-Diabetes-Detection/
│
├── app.py # Main Flask application
├── utils.py # Model loading and helper functions
│
├── models/ # Saved ML models
│ ├── diabetes_model.pkl
│ └── scaler.pkl
│
├── data/
│ └── diabetes.csv # Dataset
│
├── templates/ # Web pages
│ ├── index.html # Input form (frosted-glass UI)
│ └── report.html # Personalized health report
│
├── requirements.txt # Python dependencies
└── README.md # Project documentation
</pre>

## ⚙️ Setup Instructions
1. **Clone Repository**
   ```bash
   git clone https://github.com/DG3-here/Early-Diabetes-Detection.git
   cd "Early Diabetes Detection"

2. **Create a virtual environment (optional but recommended)**
    ```bash
    python -m venv venv
    venv\Scripts\activate   # On Windows
    source venv/bin/activate   # On macOS/Linux

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt

4. **Run the app**
    ```bash
    python app.py

5. **Open in browser**
    ```bash
    http://localhost:5000
