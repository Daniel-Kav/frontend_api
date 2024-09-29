from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView,ListView,DeleteView
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

    template_name = 'geeks/sample.html'

class GeeksList(ListView):
    # specify the model for list fecthing
    model = SampleModel

    template_name = 'geeks/list.html'