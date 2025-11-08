from flask import Flask, render_template, request
import numpy as np
from utils import load_model

app = Flask(__name__)
model, scaler = load_model()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract form data
        form_data = request.form.to_dict()
        gender = form_data.pop("Gender", "unspecified").capitalize()

        # Convert remaining numeric form fields to floats
        features = [float(value) for value in form_data.values()]
        final_features = np.array(features).reshape(1, -1)

        # Scale features and predict
        scaled_features = scaler.transform(final_features)
        prediction = model.predict(scaled_features)[0]

        # 🧠 Determine result
        emoji = "🧍‍♂️" if gender == "Male" else "🧍‍♀️"
        result = "🩸 Diabetic" if prediction == 1 else "💚 Non-Diabetic"
        risk_level = "High" if prediction == 1 else "Low"

        # 🍎 Personalized health recommendations
        if prediction == 1:  # Diabetic
            diet = [
                "Increase intake of vegetables, whole grains, and lean proteins.",
                "Avoid sugary drinks and processed foods.",
                "Eat smaller, balanced meals regularly."
            ]
            exercise = [
                "Walk briskly for at least 30 minutes a day.",
                "Incorporate light cardio and yoga for stress control.",
                "Monitor glucose levels before and after exercise."
            ]
            precautions = [
                "Check blood sugar regularly.",
                "Consult a healthcare professional regularly.",
                "Avoid smoking or excessive alcohol."
            ]
        else:  # Non-Diabetic
            diet = [
                "Maintain a balanced diet with fruits, vegetables, and whole grains.",
                "Stay hydrated and avoid excessive sugar intake."
            ]
            exercise = [
                "Engage in 30 minutes of moderate physical activity daily.",
                "Include stretching and breathing exercises."
            ]
            precautions = [
                "Keep a regular sleep schedule.",
                "Have annual health check-ups.",
                "Continue maintaining a healthy weight."
            ]

        # Render the professional report page
        return render_template(
            "report.html",
            prediction_text=f"{emoji} Result for {gender}: {result}",
            risk_level=risk_level,
            diet=diet,
            exercise=exercise,
            precautions=precautions
        )

    except Exception as e:
        return render_template("index.html", prediction_text=f"⚠️ Error: {str(e)}")


if __name__ == '__main__':
    app.run(debug=True)
