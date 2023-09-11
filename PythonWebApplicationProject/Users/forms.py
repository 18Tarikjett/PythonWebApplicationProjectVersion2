from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# The forms can also use the inbuilt User creation form Django provides. 
# This means the fields and email are pre built models that do not need to be pre-written, as it is not custom. 

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']