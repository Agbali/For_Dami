from dataclasses import fields
import email
from unittest.util import _MAX_LENGTH
from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm 
from django.forms import ModelForm
from .models import ContactUs

class RegisterForm(UserCreationForm):    
    full_name = forms.CharField(max_length=50, required=True)    
    email = forms.EmailField(required=True)


    class Meta:
        model = User
        fields = ['username', 'full_name', 'email','password1', 'password2']

class ContactUsForm(ModelForm):
    user = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    info = forms.CharField(max_length=200, required=True)
    
    class Meta:
        model = ContactUs
        fields = ['user', 'email', 'info']
    
   


