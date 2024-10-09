from django.shortcuts import render,get_object_or_404
from rest_framework import viewsets,status
from .models import Drink
from .serializers import DrinkSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

class DrinkView(viewsets.ModelViewSet):
    serializer_class = DrinkSerializer
    queryset = Drink.objects.all()

# @api_view(['GET','POST'])
# def drink_list(request):
#     #get all the objects
#     #serialize them 
#     #return a json object
#     if request.method == 'GET':
#         drinks = Drink.objects.all()
#         serializer = DrinkSerializer(drinks, many = True)
#         return JsonResponse({ 'drinks': serializer.data}, safe=False)


#     if request.method == 'POST':
#         serializer = DrinkSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

# @api_view(['GET', 'PUT','DELETE'])
# def drink_detail(request,pk):
#     drink = get_object_or_404(Drink, pk=pk)

#     if request.method == 'GET':
#         serializer = DrinkSerializer(drink)
#         return Response(serializer.date, status=status.HTTP_200_OK)
#     if request.method == 'PUT':
#         pass
#     if request.method == 'DELETE':
#         pass

@api_view(['GET','POST'])
def drink_list(request, format = None):
    drinks = Drink.objects.all()
    if request.method == 'GET':
        serializer = DrinkSerializer(drinks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = DrinkSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def drink_detail(request, pk, format = None):
    drink = get_object_or_404(Drink, pk=pk)

    if request.method == 'GET':
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = DrinkSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        