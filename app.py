import streamlit as st
import joblib
import numpy as np

# Load the trained model
reg_model = joblib.load('reg_model.pkl')

# Page title
st.title("California Housing Price Prediction")

# Sidebar for user inputs
st.sidebar.header("User Input Parameters")

def user_input_features():
    MedInc = st.sidebar.slider('MedInc', 0.0, 15.0, 5.0)
    HouseAge = st.sidebar.slider('HouseAge', 0, 52, 20)
    AveRooms = st.sidebar.slider('AveRooms', 0.0, 50.0, 5.0)
    AveBedrms = st.sidebar.slider('AveBedrms', 0.0, 10.0, 2.0)
    Population = st.sidebar.slider('Population', 0, 50000, 1000)
    AveOccup = st.sidebar.slider('AveOccup', 0.0, 50.0, 3.0)
    Latitude = st.sidebar.slider('Latitude', 32.0, 42.0, 34.0)
    Longitude = st.sidebar.slider('Longitude', -125.0, -114.0, -120.0)
    data = {
        'MedInc': MedInc,
        'HouseAge': HouseAge,
        'AveRooms': AveRooms,
        'AveBedrms': AveBedrms,
        'Population': Population,
        'AveOccup': AveOccup,
        'Latitude': Latitude,
        'Longitude': Longitude
    }
    features = np.array([list(data.values())])
    return features

input_df = user_input_features()

# Prediction
if st.button('Predict'):
    prediction = reg_model.predict(input_df)
    st.write(f'Predicted House Price: {prediction[0]:.2f}')

