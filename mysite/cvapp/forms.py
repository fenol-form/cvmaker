from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from .models import *


class AddCVForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = "__all__"


class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1')