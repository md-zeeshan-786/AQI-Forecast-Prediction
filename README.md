Air Quality Index(AQI) Prediction Using MAchine Learning



Description:-

This repository contains a Flask-based web application that predicts Air Quality Index (AQI) from common air-pollutant measurements (PM2.5, PM10, NO2, CO, SO2, O3) using Random Forest models. The app ships with pre-trained model files and a frontend that accepts pollutant inputs and displays the predicted AQI and category.


Features :-

Web UI (Flask + simple HTML/CSS/JS) to enter pollutant readings and get AQI prediction.
Pre-trained model files included: rf_model_aqi.pkl and rf_model_bucket.pkl (Random Forest regressor & classifier).
Client-side validation for inputs (JS checks positive numbers).


Tech stack :-

* Python 3.8+ (recommended)
* Flask
* scikit-learn
* pandas
* joblib


Quick start - run the app locally (use the included models) :-

1. Clone repository (or upload files to your environment)

2. Create and activate virtual environment (optional but recommended):

python -m venv venv
# macOS / Linux
source venv/bin/activate
# Windows (PowerShell)
venv\Scripts\activate.bat
or
.\venv\Scripts\Activate.ps1


3. Insatll Random Forest models :-

location:-  AQI-Forecast-Prediction > rf_model.pkl
                                    rf_model_aqi.pk
                                    rf_model_bucket.pkl
mkdir -p models
curl -L -o models/rf_model.pkl        "https://github.com/YOUR_GITHUB_USER/REPO_NAME/releases/download/v1.0/rf_model.pkl"
curl -L -o models/rf_model_aqi.pkl    "https://github.com/YOUR_GITHUB_USER/REPO_NAME/releases/download/v1.0/rf_model_aqi.pkl"
curl -L -o models/rf_model_bucket.pkl "https://github.com/YOUR_GITHUB_USER/REPO_NAME/releases/download/v1.0/rf_model_bucket.pkl"

4. Install dependencies:-

pip install -r AQI/requirements.txt


5. Run the Flask app (from inside AQI folder):-

cd AQI
python app.py

Open your browser at http://127.0.0.1:5000/ to use the web UI.

or

run step by step by opening Index.html file:-

i. Home.html -> SignIn to Start predicting
ii. Login.html -> SignIn / SignUp 
iii. Prediction.html -> Predict the AQI by entering float values for > PM2.5, PM10, NO2, CO, SO2, O3
iv. Performance Analysis -> Check performance for AQI 
v. About Us -> Our Mission & Vision 
vi. contact -> Feedback & Follow


6. How the model & UI expect inputs :-

The model features are (in this order):

PM2.5 (float)
PM10 (float)
NO2 (float)
CO (float)
SO2 (float)
O3 (float)