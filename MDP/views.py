from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import pickle
import numpy as np
from apps.models import Feedback


@login_required
def HomePage(request):
    return render(request, 'home.html', {})


def Register(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('pass')

        new_user = User.objects.create_user(name, email, password)
        new_user.save()
        return redirect('login')

    return render(request, 'register.html', {})


def Login(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        password = request.POST.get('pass')

        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('Error, user does not exist')

    return render(request, 'login.html', {})


def logoutuser(request):
    logout(request)
    return redirect('login')




# Load the saved model
RF_pkl_filename = 'RandomForest.pkl'  # Replace with the path to your .pkl file
with open(RF_pkl_filename, 'rb') as Model_pkl:
    loaded_model = pickle.load(Model_pkl)

def predict(request):
    result = None

    if request.method == 'POST':
        # Retrieve user input from the frontend form
        age = float(request.POST['age'])
        bp = float(request.POST['blood_pressure'])
        sugar = float(request.POST['sugar'])
        blood_urea = float(request.POST['blood_urea'])
        sodium = float(request.POST['sodium'])
        potassium = float(request.POST['potassium'])
        hemoglobin = float(request.POST['hemoglobin'])
        hypertension = float(request.POST['hypertension'])
        # Add more fields as needed

        # Prepare the input data for prediction
        input_data = [age, bp, sugar, blood_urea, sodium, potassium, hemoglobin, hypertension]  # Adjust this according to your model's input features
        input_data_as_array = np.asarray(input_data)
        input_data_reshaped = input_data_as_array.reshape(1, -1)

        # Make prediction using the loaded model
        prediction = loaded_model.predict(input_data_reshaped)


    return render(request, 'home.html', {'result': prediction})



def feedback(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phonenumber = request.POST['phonenumber']
        feedback = request.POST['feedback']
        ins = Feedback(name=name, email=email, phonenumber=phonenumber, feedback=feedback)
        ins.save()
        print("ok")
    return render(request, 'feedback.html', {})


def contact(request):
    return render(request, 'contact.html',{})


def precautions(request):
    return render(request, 'p.html',{})