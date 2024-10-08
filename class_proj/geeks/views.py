from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView,ListView,DeleteView,DetailView,UpdateView
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
    success_url = reverse_lazy('list')

class GeeksList(ListView):
    # specify the model for list fecthing
    model = SampleModel

    template_name = 'geeks/list.html'

class GeeksDetail(DetailView):

    model = SampleModel

    template_name = 'geeks/detail.html'

class GeeksUpdate(UpdateView):
    model = SampleModel
    fields = ['title', 'description', ]

    template_name = 'geeks/update.html'
    success_url = "/list"

class GeeksDelete(DeleteView):
    model = SampleModel
    template_name = 'geeks/delete.html'
    success_url = reverse_lazy("list")