from django import forms
from .models import MovieMod


class MovieForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = MovieMod
