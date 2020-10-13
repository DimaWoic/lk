from django import forms
from .models import InstaLikeBot
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError


class BotForm(forms.ModelForm):
    class Meta:
        model = InstaLikeBot
        fields = '__all__'


class RegForm(forms.ModelForm):
    username = forms.CharField(max_length=50, label='Логин')
    first_name = forms.CharField(max_length=250, label='Имя')
    last_name = forms.CharField(max_length=250, label='Фамилия')
    password1 = forms.CharField(label='пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='пароль, ещё один раз', widget=forms.PasswordInput,
                                help_text='Введите пароль ещё раз')

    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        if password1:
            password_validation.validate_password(password1)
        return password1

    def clean(self):
        super().clean()
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            errors = {'password2': ValidationError('Пароли не совпадют', code='password_mismatch')}
            raise ValidationError(errors)

    def clean_username(self):
        username = self.cleaned_data['username']
        list_users = []
        for u in User.objects.all():
            list_users.append(u.username)
        if username in list_users:
            raise ValidationError('Пользователь с таким логином уже существует', code='invalid')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        mails = []
        for e in User.objects.all():
            mails.append(e.email)
        if email in mails:
            raise ValidationError('Пользователь с такой электронной почтой уже существует', code='invalid')
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_active = True
        user.is_activated = True
        user.is_superuser = False
        if commit:
            user.save()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
