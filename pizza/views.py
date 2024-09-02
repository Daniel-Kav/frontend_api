from django.shortcuts import render
from .forms import PizzaForm
# Create your views here.
def home(request):
    return render(request , 'pizza/home.html')

def order(request):
    return render(request , 'pizza/order.html', {'orderform':PizzaForm()})