from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'description']

# class BlogForm(forms.ModelForm):
#     class Meta:
#         model = Blog
#         fields = ['username','email', 'password1', 'password2']