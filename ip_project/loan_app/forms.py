from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LenderSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name' , 'last_name' ,'username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user


class BorrowerSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name' , 'last_name','username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user
