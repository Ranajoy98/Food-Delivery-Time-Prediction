# Food Delivery Time Prediction

## Project Overview

This project aims to predict food delivery times based on various features such as delivery personnel attributes, location details, and order specifics. It utilizes machine learning techniques to analyze travel metrics and estimate delivery durations.

## Data Source

- The dataset used for this project is obtained from [Statso.io](https://statso.io/food-delivery-time-prediction-case-study/).

## Features

### 1. Delivery Person Attributes:

- Age
- Ratings

### 2. Location Details:

- Restaurant latitude and longitude
- Delivery location latitude and longitude

### 3. Order Details:

- Type of order (e.g., snack, buffet)
- Type of vehicle used for delivery

### 4. Travel Metrics:

- Distance between restaurant and delivery location (computed using geodesic distance)
- Speed of delivery
- Delivery time (Target Variable)

## Installation and Setup

### Prerequisites

Ensure you have Python installed along with the required libraries. You can install the dependencies using:

```sh
pip install -r requirements.txt
```

### Required Libraries:

- pandas
- numpy
- matplotlib
- seaborn
- joblib
- scikit-learn
- geopy
- Flask

## Data Preprocessing

- Checked for missing and duplicate values
- Computed the distance between restaurant and delivery location
- Derived speed using the formula:
  ```python
  data['Speed'] = data['Distance_km'] / data['Time_taken(min)']
  ```

## Exploratory Data Analysis (EDA)

- Distribution of delivery person ratings
- Distribution of delivery times
- Order and vehicle type count plots
- Scatter plot for distance vs. time taken
- Correlation heatmap
- Box plot for ratings by age

## Model Training

- Selected important features:
  ```python
  feature_columns = ["Delivery_person_Age", "Delivery_person_Ratings", "Distance_km", "Speed"]
  ```
- Used Random Forest Classifier:
  ```python
  rf_classifier = RandomForestClassifier(n_estimators=5, criterion='gini', random_state=1)
  ```
- Trained the model and evaluated using:
  - Accuracy Score
  - Confusion Matrix
  - Classification Report
  - Actual vs. Predicted Plot
- Saved the trained model using `joblib`
  ```python
  joblib.dump(rf_classifier, "random_forest_classifier.pkl")
  ```

## Flask Web App

A simple Flask application was created to allow users to input details and predict the estimated delivery time.

### Running the Web App

```sh
python app.py
```

The web application will be accessible at:

```
http://127.0.0.1:5000/
```

### Flask Routes

- `/` - Renders the homepage with an input form
- `/predict` - Accepts input, processes the data, and returns the predicted delivery time

## File Structure

```
Food-Delivery-Time-Prediction/
│
├── data/                          # Dataset (if applicable)
├── static/                        # Static files (CSS, JS, Images)
├── templates/
│   ├── index.html                 # Input form page
│   ├── result.html                 # Result display page
│
├── app.py                         # Flask Web App
├── model_training.ipynb            # Jupyter Notebook for model training
├── random_forest_classifier.pkl    # Saved model
├── requirements.txt                # Required libraries
├── README.md                       # Project Documentation
```

## License

This project is licensed under the MIT License.

