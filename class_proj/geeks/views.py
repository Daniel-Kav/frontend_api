from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView
from .models import SampleModel

# Create your views here.
class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'geeks/home.html')
    
class GeeksCreate(CreateView):
    #specify the model for view creation
    model = SampleModel

    #specify fields to be displayed
    fields = ['title', 'description', ]