from django.shortcuts import render
from .models import Blog
from .forms import BlogForm

# Create your views here.
def BlogListView(request):
    Blog_list = Blog.objects.all()
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'blog/blog_list.html', {"bloglist":Blog_list,'form':form })