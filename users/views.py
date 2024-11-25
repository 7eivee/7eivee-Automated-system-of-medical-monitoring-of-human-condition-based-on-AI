# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegisterForm
import json
import joblib
import pandas as pd
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def register_view(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()  # Сохраняем пользователя в базе данных
            messages.success(request, "Регистрация прошла успешно! Пожалуйста, войдите в аккаунт.")
            return redirect('users:login')  # Перенаправляем на страницу входа

    return render(request, 'main/index.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            patients = [
                {
                    'id': 1,
                    'full_name': 'Іван Іванович',
                    'age': 30,
                    'gender': 'Чоловік',
                    'dob': '1994-05-12',
                    'treatment_location': 'Київ',
                    'weight': 70,
                    'height': 175,
                    'ip_device': 'F2-H5-83-T3'
                },
                {
                    'id': 2,
                    'full_name': 'Олена Петрівна',
                    'age': 25,
                    'gender': 'Жінка',
                    'dob': '1999-02-15',
                    'treatment_location': 'Львів',
                    'weight': 60,
                    'height': 165,
                    'ip_device': 'C5-G1-33-U0'
                },
                {
                    'id': 3,
                    'full_name': 'Андрій Олексійович',
                    'age': 40,
                    'gender': 'Чоловік',
                    'dob': '1984-10-20',
                    'treatment_location': 'Одеса',
                    'weight': 80,
                    'height': 180,
                    'ip_device': 'X6-J3-21-L1'
                }
            ]
            print("activate")
            return render(request, 'users/login.html', {'patients': patients})  # Или другой URL для перенаправления после успешного входа
        else:
            patients = [
                {
                    'id': 1,
                    'full_name': 'Іван Іванович',
                    'age': 30,
                    'gender': 'Чоловік',
                    'dob': '1994-05-12',
                    'treatment_location': 'Київ',
                    'weight': 70,
                    'height': 175,
                    'status': 'On',
                    'ip_device': 'F2-H5-83-T3',
                    'heart_rate':72,
                    'blood_pressure':120,
                    'spO2':98,
                    'glucose_level':5.5,
                    'temperature':36.6,

                },
                {
                    'id': 2,
                    'full_name': 'Олена Петрівна',
                    'age': 25,
                    'gender': 'Жінка',
                    'dob': '1999-02-15',
                    'treatment_location': 'Львів',
                    'weight': 60,
                    'height': 165,
                    'status': 'On',
                    'ip_device': 'C5-G1-33-U0',
                    'heart_rate':72,
                    'blood_pressure':120,
                    'spO2':98,
                    'glucose_level':5.5,
                    'temperature':36.6,
                },
                {
                    'id': 3,
                    'full_name': 'Андрій Олексійович',
                    'age': 65,
                    'gender': 'Чоловік',
                    'dob': '1984-10-20',
                    'treatment_location': 'Одеса',
                    'weight': 80,
                    'height': 180,
                    'status': 'On',
                    'ip_device': 'X6-J3-21-L1',
                    'heart_rate':90,
                    'blood_pressure':140,
                    'spO2':95,
                    'glucose_level':5.5,
                    'temperature':36.6,
                }
            ]
            message = "Неверный логин или пароль. Попробуйте снова."
            return render(request, 'users/login.html', {'patients': patients})
    
    return render(request, 'users/login.html')

def add_patient_view(request):
    # Логика для добавления пациента
    return render(request, 'users/add_patient.html')

def patient_details(request, id):
    # Получаем пациента по ID или возвращаем 404, если он не найден
    return render(request, 'users/patient_details.html', {'patient': 1})


model_path = 'C:/Users/jekaa/diplom_project/users/templates/users/disease_prediction_models.pkl'
models = joblib.load(model_path)

@csrf_exempt  
def analyze_patient(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        patient_data = {
            'age': [int(data['age'])],
            'gender': [int(data['gender'])],
            'heart_rate': [int(data['heart_rate'])],
            'blood_pressure': [int(data['blood_pressure'])],
            'spO2': [int(data['spO2'])],
            'glucose_level': [float(data['glucose_level'])],
            'temperature': [float(data['temperature'])]
        }
        patient_df = pd.DataFrame(patient_data)

        predictions = {}
        for disease, model in models.items():
            disease_proba = model.predict_proba(patient_df)[:, 1][0]
            predictions[disease] = {
                'Prediction': 'Yes' if disease_proba >= 0.5 else 'No',
                'Probability': float(round(disease_proba, 2))
            }

        return JsonResponse({'predictions': predictions})