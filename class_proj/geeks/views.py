from django.shortcuts import render,HttpResponse
from django.views import View

# Create your views here.
class HomeView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("<h1>This is Home</h1>")