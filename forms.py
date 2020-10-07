from django import forms
from .models import InstaLikeBot


class BotForm(forms.ModelForm):
    class Meta:
        model = InstaLikeBot
        fields = '__all__'
