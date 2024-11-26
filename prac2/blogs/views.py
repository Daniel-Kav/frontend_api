from django.shortcuts import render,redirect,get_object_or_404
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

def editBlog(request,pk):
    blog = get_object_or_404(Blog, pk=pk)

    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    else:
        form = BlogForm(instance=blog)
    return render(request,'editBlog.html',{'form': form})

def deleteBlog(request,pk):
    blog = get_object_or_404(Blog, pk=pk)

    if request.method == 'POST':
        blog.delete()
        return redirect('home')
    return render(request, 'delete.html')





