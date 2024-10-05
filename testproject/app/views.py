from django.shortcuts import render,redirect, get_object_or_404
from .models import Post,Comment
from .forms import PostForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'home.html', context)

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit= False)
            post.author = request.user
            post.save()
            return redirect("home")
    else:
        form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'post.html', context)



def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    return render(request, 'detail.html', {'post': post})