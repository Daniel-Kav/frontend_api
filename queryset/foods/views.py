from django.shortcuts import render
from .models import Food
from django.views.generic import ListView

# Create your views here.
def  home(request):
    foods = Food.objects.all()
    return render(request, 'home.html', {'foods': foods})

class HomeView(ListView):
    model = Food
    template_name = 'home.html'