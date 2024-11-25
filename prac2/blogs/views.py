from django.shortcuts import render,redirect
from .models import Blog
from .forms import BlogForm

# Create your views here.
def getBlogs(request):
    blogs = Blog.objects.all()
    return render(request,'home.html',{'blogs':blogs})

def addBlog(request):
    if request.method == 'POST':
        blog = BlogForm(request.POST)

        if blog.is_valid():
            blog.save()
            return redirect('home')
    else:
        blog = BlogForm()
    return render(request,'addblog.html',{'blog':blog})


