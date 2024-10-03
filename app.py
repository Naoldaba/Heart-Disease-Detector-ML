from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the trained model
model = joblib.load('heartDiseasePredictor.pkl')

# Initialize the flask app
app = Flask(__name__)


def preprocess_input(data):
    # convert the input data to a DataFrame
    df = pd.DataFrame([data])
    scaler = StandardScaler()

    # numeric cols that need scaling
    cols_to_scale = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
    
    # scale the numeric columns
    df[cols_to_scale] = scaler.fit_transform(df[cols_to_scale])
    
    return df

# Route handler
@app.route('/heart_disease/predict', methods=['POST'])
def predict():
    try:
        input_data = request.json
        preprocessed_data = preprocess_input(input_data)

        # perform prediction 
        prediction = model.predict(preprocessed_data)

        res = "Heart disease found" if int(prediction[0]) == 1 else "No heart disease found"
        return jsonify({'prediction': res})

    except Exception as e:
        return jsonify({'error': str(e)})

# Entry point
if __name__ == '__main__':
    app.run(debug=True)
