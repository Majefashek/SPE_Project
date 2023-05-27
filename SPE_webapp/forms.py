from django.contrib.auth.forms import UserCreationForm
from account.models import CustomUser
from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image')
        exclude = ('user',)

