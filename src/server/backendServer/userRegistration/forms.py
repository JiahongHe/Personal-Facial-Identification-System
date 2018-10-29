from django import forms
from django.apps import apps
from django.forms import ModelForm
from requestHandler.models import User

class registrationForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'FirstName',
            'LastName',
            'Gender',
            'Image',
            'FavouriteSong',
            'Email'
        ]
