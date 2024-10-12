from django.shortcuts import render
from rest_framework import generics
from .models import Publisher,Author,Book
from .serializers import PublisherSerializer,AuthorSerializer,BookSerializer

# Create your views here.
# list and create publishers
class PublisherCreateView(generics.ListCreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

