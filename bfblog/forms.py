from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import SuperUser, BlogPost

class BlogPostForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 30,
        'cols': 200, 
    }))

    class Meta:
        model = BlogPost
        fields = ('__all__')

class SuperUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = SuperUser
        fields = '__all__'


class SuperUserChangeForm(UserChangeForm):
    class Meta:
        model = SuperUser
        fields = '__all__'