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

def BlogUpdate(request, pk):
    blog = Blog.objects.get(pk=pk)
    form = BlogForm(request.POST)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog-list')
    return render(request, 'blog/blog_update.html', {'form':form, 'blog':blog})


def BlogDelete(request,pk):
    blog = Blog.objects.get(pk=pk)
    if request.method == 'POST' :
        blog.delete()
        return redirect('blog-list')
    return render(request, 'blog/blog_delete_confirmation.html', {'blog': blog})