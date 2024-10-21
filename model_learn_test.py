import joblib
import pandas as pd
import numpy as np

# Load the saved model and scaler
model = joblib.load('best_crop_prediction_model.pkl')
scaler = joblib.load('scaler.pkl')

# Function to predict the crop based on input values
def predict_crop(N, P, K, pH, temperature):
    # Create a DataFrame with the input values
    input_data = pd.DataFrame([[N, P, K, pH, temperature]], columns=['N', 'P', 'K', 'temperature', 'ph'])
    
    # Standardize the input data
    input_data_scaled = scaler.transform(input_data)
    
    # Make a prediction
    prediction = model.predict(input_data_scaled)
    
    return prediction[0]

# Example usage
N = 5
P = 74
K = 21
pH = 16.245
temperature = 5.592

#5,74,21,16.245,5.592 = kidneybeans

predicted_crop = predict_crop(N, P, K, pH, temperature)
print(f'The predicted crop is: {predicted_crop}')
