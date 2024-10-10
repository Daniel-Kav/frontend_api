from django.shortcuts import render, get_object_or_404
from .serializers import RecipeSerializer
from .models import Recipe
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.
@api_view(['GET', 'POST'])
def recipe_list(request):
    recipes = Recipe.objects.all()
    if request.method == 'GET':
        serializer = RecipeSerializer(recipes, many= True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = RecipeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)

    if request.method == 'GET':
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        serializer = RecipeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
