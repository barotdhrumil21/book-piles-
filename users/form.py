from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegForm(UserCreationForm):
    email = forms.EmailField()
    last_name=forms.CharField(max_length=100)

    class Meta: 
        model = User  #where to submit the data (basically name of the database)
        fields = ['username','last_name', 'email', 'password1', 'password2']