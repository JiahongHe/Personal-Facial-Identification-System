from django.apps import apps
from django.forms import ModelForm
from django import forms
from requestHandler.models import User

class registrationForm(ModelForm):
    confirm_passWord = forms.CharField(widget=forms.PasswordInput())
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

    def clean(self):
        cleaned_data = super(registrationForm, self).clean()
        password = cleaned_data.get("passWord")
        confirm_password = cleaned_data.get("confirm_passWord")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm password does not match"
            )