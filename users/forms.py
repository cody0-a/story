from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
#from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label = "Password",widget=forms.PasswordInput)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "Username"
        self.fields['password'].label = "Password"

    