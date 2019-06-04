from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import SuperUser

class SuperUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = SuperUser
        fields = '__all__'

class SuperUserChangeForm(UserChangeForm):
    
    class Meta:
        model = SuperUser
        fields = '__all__'