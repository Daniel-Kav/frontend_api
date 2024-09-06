from django.shortcuts import render,redirect,get_object_or_404
from .models import Blog,Post, Comment
from .forms import BlogForm,CommentForm, PostForm
from django.contrib.auth.decorators import login_required

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
    form = BlogForm(request.POST, instance=blog)
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

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        comment_form = CommentForm()
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form})

@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author:
        return redirect('post_detail', pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user == post.author:
        post.delete()
    return redirect('post_list')