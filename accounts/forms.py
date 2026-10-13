from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

User_Model = get_user_model()


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User_Model
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        ]


class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update(
            {
                "type": "text",
                "required class": "w-full px-4 py-2.5 text-sm bg-slate-50 border border-slate-300 rounded-xl focus:ring-2 focus:ring-indigo-500 outline-none",
                "placeholder":"Enter your username"
            }
        )

        self.fields["password"].widget.attrs.update(
            {
               "type":"password",
                "required class":"w-full px-4 py-2.5 text-sm bg-slate-50 border border-slate-300 rounded-xl focus:ring-2 focus:ring-indigo-500 outline-none",
                "placeholder":"Enter your Password"

            }
        )
