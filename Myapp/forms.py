# forms.py
from django import forms

class LoginForm(forms.Form):
    email_or_phone = forms.CharField(max_length=255)