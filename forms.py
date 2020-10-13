from django import forms
from .models import InstaLikeBot
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class BotForm(forms.ModelForm):
    class Meta:
        model = InstaLikeBot
        fields = '__all__'


class RegForm(UserCreationForm):
    email = forms.EmailField()
    username = forms.CharField(max_length=250, label='Логин')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
    
