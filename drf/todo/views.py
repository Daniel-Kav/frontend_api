from django.shortcuts import render
from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer

# Create your views here.
class TodoView(viewsets.ModelViewSet):
    #create a serializer class and assign it to the todo serializer
    serializer_class = TodoSerializer
    #define a var and populate it with todo data
    queryset = Todo.objects.all()
