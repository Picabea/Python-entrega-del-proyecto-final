from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username', 
            'email', 
            'password1', 
            'password2'
            ]

class UserEditForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username', 
            'email', 
            'password1', 
            'password2'
        ]
        help_texts = {k: '' for k in fields}

class PerfilForm(forms.Form):
    avatar = forms.URLField()
    descripcion = forms.CharField(max_length=150)
    link = forms.URLField()

