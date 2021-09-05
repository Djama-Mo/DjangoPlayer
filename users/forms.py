from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Profile
        fields = ['username', 'email', 'password1', 'password2']

