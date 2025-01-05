### How to run the application
Start the app by running the following command in your terminal:
python app.py

# Homepage (index.html):
Users input the required data for prediction (age, ratings, distance, speed).
The form submits data to the /predict endpoint via a POST request.

# Backend (app.py):
Flask retrieves the form data, preprocesses it into a Pandas DataFrame, and uses the Random Forest model to make a prediction.

# Result Page (result.html):
Displays the prediction in minutes along with an option to return to the homepage.

