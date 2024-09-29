from django.forms import ModelForm
from .models import SampleModel


class SampleModelForm(ModelForm):
    class Meta:
        model = SampleModel
        fields = ['title', 'description']