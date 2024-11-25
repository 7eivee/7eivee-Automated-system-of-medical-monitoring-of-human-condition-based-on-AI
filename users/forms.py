from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    user_type = forms.ChoiceField(choices=[('doctor', 'Лікар'), ('patient', 'Пацієнт')], widget=forms.RadioSelect)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'user_type', 'full_name', 'age', 'gender', 'dob', 'treatment_location', 'weight', 'height']

    def save(self, commit=True):
        user = super().save(commit=False)
        user_type = self.cleaned_data.get('user_type')
        user.is_doctor = user_type == 'doctor'
        user.is_patient = user_type == 'patient'
        if commit:
            user.save()
        return user
