import pickle
import numpy as np
import pyttsx3
import speech_recognition as sr

# Load the saved model
RF_pkl_filename = 'RandomForest.pkl'  # Replace with the path to your .pkl file
with open(RF_pkl_filename, 'rb') as Model_pkl:
    loaded_model = pickle.load(Model_pkl)

# Set feature names (if available)
if hasattr(loaded_model, 'set_feature_names'):
    feature_names = ['Fever', 'Cough', 'Fatigue', 'Difficulty Breathing', 'Age', 'Gender', 'Blood Pressure', 'Cholesterol Level']
    loaded_model.set_feature_names(feature_names)

# Initialize Speech Recognition for English
recognizer = sr.Recognizer()

# Initialize pyttsx3 for text-to-speech
engine = pyttsx3.init()

# Set English language for text-to-speech
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\SPEECH\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')  # English voice

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_yes_no_input(prompt):
    speak(prompt)
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print(prompt)
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
    try:
        input_text = recognizer.recognize_google(audio, language='en-US')
        print(f"User input: {input_text}")
        return input_text.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Please speak clearly.")
        return get_yes_no_input(prompt)
    except sr.RequestError:
        speak("Sorry, there was an error processing your request.")
        return None

while True:
    Fever = get_yes_no_input("Do you have fever? Say 'yes' or 'no'")
    Fever = 1 if 'yes' in Fever else 0 if 'no' in Fever else None

    if Fever is None:
        continue

    Cough = get_yes_no_input("Do you have a cough? Say 'yes' or 'no'")
    Cough = 1 if 'yes' in Cough else 0 if 'no' in Cough else None

    if Cough is None:
        continue

    Fatigue = get_yes_no_input("Do you have fatigue? Say 'yes' or 'no'")
    Fatigue = 1 if 'yes' in Fatigue else 0 if 'no' in Fatigue else None

    if Fatigue is None:
        continue

    Breathing = get_yes_no_input("Do you have difficulty breathing? Say 'yes' or 'no'")
    Breathing = 1 if 'yes' in Breathing else 0 if 'no' in Breathing else None

    if Breathing is None:
        continue

    # Similarly, add more questions for other symptoms...

    Age = float(input("Enter your age: "))
    Gender = input("Enter your gender: ")
    Blood = input("Enter your blood pressure level (low, normal, high): ")
    Cholesterol = input("Enter your cholesterol level (low, normal, high): ")

    # Prepare the input data for prediction
    input_data = [Fever, Cough, Fatigue, Breathing, Age, Gender, Blood, Cholesterol]  # Adjust this according to your model's input features
    input_data_as_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_array.reshape(1, -1)

    # Make prediction using the loaded model
    prediction = loaded_model.predict(input_data_reshaped)

    print(prediction)  # Replace this with your appropriate action based on the prediction
