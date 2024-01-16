import pickle
import numpy as np

# Load the saved model
RF_pkl_filename = 'RandomForest.pkl'  # Replace with the path to your .pkl file
with open(RF_pkl_filename, 'rb') as Model_pkl:
    loaded_model = pickle.load(Model_pkl)

# Set feature names (if available)
if hasattr(loaded_model, 'set_feature_names'):
    feature_names = ['Fever', 'Cough', 'Fatigue', 'Difficulty Breathing', 'Age', 'Gender', 'Blood Pressure', 'Cholesterol Level']
    loaded_model.set_feature_names(feature_names)

while(True):
    Fever = input("enter the Fever: ")
    if Fever == 'yes':
        Fever = 1
    elif Fever == 'no':
        Fever = 0
    Cough = input("enter the Cough: ")
    if Cough == 'yes':
        Cough = 1
    elif Cough == 'no':
        Cough = 0
    Fatigue = input("enter the Fatigue: ")
    if Fatigue == 'yes':
        Fatigue = 1
    elif Fatigue == 'no':
        Fatigue = 0
    Breathing = input("enter the Difficulty Breathing")
    if Breathing == 'yes':
        Breathing = 1
    elif Breathing == 'no':
        Breathing = 0
    Age = float(input("enter the Age"))
    Gender = input("enter the Gender")
    if Gender == 'male':
        Gender = 1
    elif Gender == 'female':
        Gender = 0
    Blood = input("enter the Blood Pressure")
    if Blood == 'low':
        Blood = 1
    elif Blood == 'normal':
        Blood = 2
    elif Blood == 'high':
        Blood = 0
    Cholesterol = input("enter the Cholesterol Level")
    if Cholesterol == 'low':
        Cholesterol = 1
    elif Cholesterol == 'normal':
        Cholesterol = 2
    elif Cholesterol == 'high':
        Cholesterol = 0
            # Add more fields as neede
        # Prepare the input data for prediction
    input_data = [Fever, Cough, Fatigue, Breathing, Age, Gender, Blood, Cholesterol]  # Adjust this according to your model's input features
    input_data_as_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_array.reshape(1, -1)

            # Make prediction using the loaded model
    prediction = loaded_model.predict(input_data_reshaped)

    print(prediction)
