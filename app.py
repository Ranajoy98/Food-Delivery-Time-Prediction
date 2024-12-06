from flask import Flask, render_template, request
import joblib
import pandas as pd

# Load the trained model
model_filename = "random_forest.pkl"
rf_classifier = joblib.load(model_filename)

# Create a Flask app
app = Flask(__name__)

@app.route('/')
def home():
    """Render the homepage with the input form."""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Handle form submission and predict based on input."""
    try:
        # Get form data
        delivery_person_age = int(request.form['delivery_person_age'])
        delivery_person_ratings = float(request.form['delivery_person_ratings'])
        distance_km = float(request.form['distance_km'])
        speed = float(request.form['speed'])

        # Create a DataFrame for the model
        input_data = pd.DataFrame([{
            "Delivery_person_Age": delivery_person_age,
            "Delivery_person_Ratings": delivery_person_ratings,
            "Distance_km": distance_km,
            "Speed": speed
        }])

        # Make prediction
        prediction = rf_classifier.predict(input_data)[0]

        # Render result page
        return render_template('result.html', prediction=prediction)

    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)
