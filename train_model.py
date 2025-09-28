import pandas as pd
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, accuracy_score
import joblib

# Load dataset
data = pd.read_csv('city_day2.csv')

# Handle missing values
data.fillna(data.mean(), inplace=True)

# Features and targets
features = data[['PM2.5', 'PM10', 'NO2', 'CO', 'SO2', 'O3']]
target_aqi = data['AQI']
aqi_bucket_mapping = {'Good': 0, 'Satisfactory': 1, 'Moderate': 2, 'Poor': 3, 'Very Poor': 4, 'Severe': 5}
target_bucket = data['AQI_Bucket'].map(aqi_bucket_mapping)

# Split data
X_train, X_test, y_train_aqi, y_test_aqi = train_test_split(features, target_aqi, test_size=0.2, random_state=42)
_, _, y_train_bucket, y_test_bucket = train_test_split(features, target_bucket, test_size=0.2, random_state=42)

# Train AQI regressor
rf_aqi = RandomForestRegressor(n_estimators=100, random_state=42)
rf_aqi.fit(X_train, y_train_aqi)
joblib.dump(rf_aqi, 'rf_model_aqi.pkl')

# Train AQI_Bucket classifier
rf_bucket = RandomForestClassifier(n_estimators=100, random_state=42)
rf_bucket.fit(X_train, y_train_bucket)
joblib.dump(rf_bucket, 'rf_model_bucket.pkl')
