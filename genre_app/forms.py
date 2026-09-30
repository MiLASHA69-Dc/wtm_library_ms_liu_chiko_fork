from django import forms

from .models import Genre

class CreateGenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = [
            "title","category"
        ]