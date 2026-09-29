from django import forms
from .models import Author

class CreateAuthorEntry(forms.ModelForm):
    class Meta:
        model = Author
        fields = [
            "first_name",
            "last_name",
            "dob",
            "year_of_death",
        ]