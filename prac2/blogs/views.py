from django.shortcuts import render
from .models import Blog

# Create your views here.
def getBlogs(request):
    blogs = Blog.objects.all()
    return render(request,'home.html',{blogs:'blogs'})

