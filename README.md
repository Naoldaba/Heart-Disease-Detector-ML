# Heart Disease Detection

This project implements a machine learning model for predicting the presence of heart disease based on patient characteristics and medical history. The model takes various inputs related to heart health and outputs whether or not the patient is likely to have heart disease.

# Model Training

The heart disease prediction model is trained using the **Logistic Regression** algorithm, a widely used statistical method for binary classification tasks. Logistic regression estimates the probability that a given input point belongs to a certain category, in this case, whether a patient has heart disease or not.

## Dataset

The model was trained on a dataset containing various patient attributes related to heart health. The dataset includes the following features:

- **age**: Age of the patient
- **sex**: Gender (0 = female, 1 = male)
- **cp**: Chest pain type (0-3)
- **trestbps**: Resting blood pressure (in mm Hg)
- **chol**: Serum cholesterol (in mg/dl)
- **fbs**: Fasting blood sugar (0 = false, 1 = true)
- **restecg**: Resting electrocardiographic results (0-2)
- **thalach**: Maximum heart rate achieved
- **exang**: Exercise induced angina (0 = no, 1 = yes)
- **oldpeak**: ST depression induced by exercise relative to rest
- **slope**: Slope of the peak exercise ST segment (0-2)
- **ca**: Number of major vessels (0-3) colored by fluoroscopy
- **thal**: Thalassemia (0-3)

## Technologies

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy

## Installation

1. Clone the repository:

- https://github.com/Naoldaba/Heart-Disease-Detector-ML.git
- cd heart_disease_detector


## Usage

1. Run the Flask server:

- python app.py

2. The server will start on `http://127.0.0.1:5000`.

3. You can now make predictions by sending a POST request to the `/heart_disease/predict` endpoint.


## API Endpoints

### Predict

- **URL**: `/heart_disease/predict`
- **Method**: `POST`
- **Request Body**: JSON object containing the following fields:

```json
{
 "age": 71,
 "sex": 0,
 "cp": 0,
 "trestbps": 112,
 "chol": 149,
 "fbs": 0,
 "restecg": 1,
 "thalach": 125,
 "exang": 0,
 "oldpeak": 1.6,
 "slope": 1,
 "ca": 0,
 "thal": 2
}