from django import forms
from auth_signup.models import User


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name']
        widgets = {
            'password': forms.PasswordInput(),
        }
