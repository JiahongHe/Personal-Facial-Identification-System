from django.apps import apps
from django.forms import ModelForm
from django import forms
from .models import User

class updateForm(ModelForm):
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