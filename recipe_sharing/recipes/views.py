from django.shortcuts import render
from .serializers import RecipeSerializer
from .models import Recipe
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

def recipe_list(request):
    recipes = Recipe.objects.all()
    serializer = RecipeSerializer(recipes, many= True)
    return Response(serializer.data, status=status.HTTP_200_OK)
