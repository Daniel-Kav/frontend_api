from django.shortcuts import render
from .models import Food

# Create your views here.
def  home(request):
    foods = Food.objects.all()
    return render(request, 'home.html', {'foods': foods})