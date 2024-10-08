from django import forms
from .models import Sample

class SampleForm(forms.ModelForm):
    class Meta:
        model = Sample
        fields = ['title', 'description']