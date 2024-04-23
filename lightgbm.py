import requests
from PIL import Image
import numpy as np
import lightgbm as lgb
import pickle

def fetch_image(url):
    response = requests.get(url)
    if response.status_code == 200:
        return Image.open(BytesIO(response.content))
    else:
        raise Exception(f"Failed to fetch image from {url}")

def preprocess_image(image):
    # Placeholder for image preprocessing
    # This should match how your model was trained
    # For example, resizing, converting to grayscale, etc.
    return np.array(image)

def predict_cyanobacteria_density(image_url):
    # Load the trained LightGBM model
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
    
    # Fetch the image
    image = fetch_image(image_url)
    
    # Preprocess the image
    features = preprocess_image(image)
    
    # Reshape the features to match the model's input shape
    # This step depends on how your model was trained
    # For example, if your model expects a 2D array of shape (1, n_features)
    features = features.reshape(1, -1)
    
    # Predict cyanobacteria density
    prediction = model.predict(features)
    
    return prediction