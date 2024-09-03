from django import forms

from .models import Task

class Task(forms.ModelForm):
    class Meta:
        model = Task
        fields =['title', 'completed']