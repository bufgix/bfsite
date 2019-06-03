from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import SuperUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = SuperUser
        fields = '__all__'

class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = SuperUser
        fields = '__all__'