# users/urls.py

from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('add_patient/', views.add_patient_view, name='add_patient'),
    path('patient/<int:id>/', views.patient_details, name='patient_details'),
    path('analyze_patient/', views.analyze_patient, name='analyze_patient'),
]
