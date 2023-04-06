from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    """A form for user login.

    Allows users to enter their username and password.
    """

    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    """A form for user registration.

    Allows users to create an account by entering their username, email,
    and password.
    """
    
    first_name = forms.CharField(max_length=65)
    class Meta:
        model = User
        fields = ['username','first_name','email','password1','password2']