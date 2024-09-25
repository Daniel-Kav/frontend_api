from django.shortcuts import render,redirect
from .models import Food
from django.views.generic import ListView, CreateView
from .forms import FoodForm
from django.contrib import messages
# Create your views here.
def  home(request):
    foods = Food.objects.all()
    return render(request, 'home.html', {'foods': foods})

class HomeView(ListView):
    model = Food
    template_name = 'home.html'

def add_food(request):
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'food added successfully')
            return redirect('home')
    else:
        form = FoodForm()
    return render(request, 'food.html', {'form': form})
