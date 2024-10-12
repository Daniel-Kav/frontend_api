from django.shortcuts import render
from rest_framework import generics
from .models import Publisher,Author,Book
from .serializers import PublisherSerializer,AuthorSerializer,BookSerializer

# Create your views here.
# list and create publishers
class PublisherCreateView(generics.ListCreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

# retrieve update and delete publishers
class PUblisherDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

class AuthorCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
