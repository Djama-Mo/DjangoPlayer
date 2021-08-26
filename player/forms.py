from django import forms
from .models import Genre
from .models import User


class SongForm(forms.Form):
    title = forms.CharField()
    artist = forms.CharField()
    genre = forms.ModelChoiceField(queryset=Genre.objects.all())
    user = forms.ModelChoiceField(queryset=User.objects.all())
