from django import forms
from . import models
from django.forms.widgets import DateInput, TimeInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title', 'content', 'category', 'image']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ["profile_picture", "bio"]