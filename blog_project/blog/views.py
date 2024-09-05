from django.shortcuts import render,redirect
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

def BlogDetails(request, pk):
    blog = Blog.objects.get(pk=pk)
    return render(request, 'blog/blog_details.html', {'blog':blog})

def BlogDelete(request,pk):
    blog = Blog.objects.get(pk=pk)
    if request.method == 'POST' :
        blog.delete()
        return redirect('blog-list')
    return render(request, 'blog/blog_delete_confirmation.html', {'blog': blog})