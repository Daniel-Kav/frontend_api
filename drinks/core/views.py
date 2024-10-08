from django.shortcuts import render
from rest_framework import viewsets
from .models import Drink
from .serializers import DrinkSerializer

# Create your views here.

class DrinkView(viewsets.ModelViewSet):
    serializer_class = DrinkSerializer
    queryset = Drink.objects.all()

def drink_list(request):
    #get all the objects
    #serialize them 
    #return a json object

    drinks = Drink.objects.all()
    serializer = DrinkSerializer(drinks, many = True)

    return JSONObject(serializer.data)
