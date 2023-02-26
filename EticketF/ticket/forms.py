from django import forms
from .models import *

class LoginForm(forms.Form):
    class deta:
        models = Login
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }