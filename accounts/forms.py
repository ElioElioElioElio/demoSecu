from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

FRUIT_CHOICES= [
    ('1', 'Clear'),
    ('2', 'Hashed'),
    ('3', 'Hashed & Salted'),
    ('4', 'Hashed & Salted by the user'),
    ('5', 'Symmetric encryption and Hashed & Salted by the user'),
    ]

class RegisterForm(UserCreationForm):
    
    password_management= forms.CharField(label='Password Management', widget=forms.RadioSelect(choices=FRUIT_CHOICES))
    salt= forms.CharField(label='Salt')

    class Meta:
        model = User
        fields = ["username","password_management", "password1", "password2","salt"]