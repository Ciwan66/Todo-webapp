from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import CustomUser


class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email','first_name','last_name','password1','password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254, required=True,
                            widget=forms.EmailInput(attrs={'placeholder':'Email Adress',
                                                             'class': 'form-control'}))
    password = forms.CharField(max_length=64, required=True,
                               widget=forms.PasswordInput(attrs={'placeholder':'Enter Password',
                                                             'class': 'form-control'}))
    class Meta:
        model = CustomUser
        fields = ['username','password']