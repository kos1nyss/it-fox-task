from django import forms

from django.contrib.auth.hashers  import check_password
from django.contrib.auth.models import User

from .models import *


class UserForm(forms.Form):
    id = forms.IntegerField(required=False)
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)

    def clean(self):
        user = User.objects.get(username=self.cleaned_data.get('username'))
        if not user:
            raise forms.ValidationError('Incorrect username')
        if not check_password(self.cleaned_data.get('password'), user.password):
            raise forms.ValidationError('Incorrect password')
        return self.cleaned_data


class TokenForm(forms.Form):
    token = forms.CharField(max_length=100)

    def clean_token(self):
        token = self.cleaned_data.get('token')
        print(token)
        if not Tokens.objects.all().filter(token=token):
            raise forms.ValidationError('Incorrect token')

        return token
