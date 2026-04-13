from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class SignUpForm(UserCreationForm):
    university = forms.CharField(label='학교')
    email = forms.CharField(label='이메일')
    nickname = forms.CharField(label='닉네임')
    
    class Meta:
        model = get_user_model()
        fields = ['university', 'email', 'nickname', 'username']