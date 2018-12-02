from django.apps import apps
from django.forms import ModelForm
from django import forms
from .models import User

class updateForm(ModelForm):
    confirm_passWord = forms.CharField(widget=forms.PasswordInput())
    userId = forms.IntegerField()
    class Meta:
        model = User
        fields = [
            'FirstName',
            'LastName',
            'Image',
            'FavouriteSong',
            'Email',
            'passWord']
        widgets = {
        'passWord': forms.PasswordInput(),
        }