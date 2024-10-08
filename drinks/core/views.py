from django.shortcuts import render
from rest_framework import viewsets
from .models import Drink
from .serializers import DrinkSerializer

# Create your views here.

class DrinkView(viewsets.ModelViewSet):
    serializer_class = DrinkSerializer
    queryset = Drink.objects.all()
