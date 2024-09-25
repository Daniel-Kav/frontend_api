from django.shortcuts import render,redirect,get_object_or_404
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
            messages.error(request, 'fill the form with the correct values')
    else:
        form = FoodForm()
    return render(request, 'food.html', {'form': form})

# def edit_food(request, pk):
#     food = get_object_or_404(Food, pk=pk)
#     if request.method == 'POST':
#         form = FoodForm(request.POST ,instance=food)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'food successfully edited')
#             return redirect('home')
#     else:
#         form = FoodForm(initial= food)
#         messages.error(request, 'food not found')
#         return render(request, 'edit_food.html', {'form': form})

def edit_food(request, pk):
    food = Food.objects.get(pk=pk)
    if request.method == 'POST':
        form = FoodForm(request.POST , instance=food)
        if form.is_valid():
            form.save()
            messages.success(request,'food updated successfully')
            return redirect('home')
    else:
        form = FoodForm(instance=food)
    return render(request, 'edit_food.html',{'form':form})

def delete_food(request, pk):
    food = get_object_or_404(Food, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete_food.html',{'pk':pk})
    if request.method == 'POST':
        food.delete()
        messages.success(request, 'food deleted successfully')