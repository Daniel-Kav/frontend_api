from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    model = Blog
    fields = ['title', 'description']