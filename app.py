from flask import Flask, render_template, request
import joblib

# Initialize Flask app
app = Flask(__name__)

# Load trained models
rf_aqi = joblib.load('rf_model_aqi.pkl')  # Model for AQI numerical prediction
bucket_mapping = {0: 'Good', 1: 'Satisfactory', 2: 'Moderate', 3: 'Poor', 4: 'Very Poor', 5: 'Severe'}

# Function to categorize AQI based on value
def categorize_aqi(aqi_value):
    if aqi_value <= 50:
        return "Good", "good"
    elif 51 <= aqi_value <= 100:
        return "Satisfactory", "satisfactory"
    elif 101 <= aqi_value <= 200:
        return "Moderate", "moderate"
    elif 201 <= aqi_value <= 300:
        return "Poor", "poor"
    elif 301 <= aqi_value <= 400:
        return "Very Poor", "very-poor"
    else:
        return "Severe", "severe"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect inputs from form
        input_data = [float(request.form[key]) for key in ['PM2.5', 'PM10', 'NO2', 'CO', 'SO2', 'O3']]

        # Predict AQI
        predicted_aqi = rf_aqi.predict([input_data])[0]

        # Map AQI value to category and CSS class
        predicted_category, category_class = categorize_aqi(predicted_aqi)

        # Debugging: Print the predicted AQI, category, and class
        print(f"Predicted AQI: {predicted_aqi}, Category: {predicted_category}, Class: {category_class}")

        # Return results to the user
        return render_template(
            'index.html',
            prediction=f"AQI: {predicted_aqi:.2f}",
            category=f"Category: {predicted_category}",
            category_class=category_class  # Pass the CSS class
        )
    except Exception as e:
        return render_template('index.html', error=f"Error: {str(e)}")



if __name__ == '__main__':
    app.run(debug=True)
