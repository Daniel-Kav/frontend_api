from django.shortcuts import render,redirect
from .models import Post,Comment
from .forms import PostForm

# Create your views here.
def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'home.html', context)

def create_post(request):
    form = PostForm
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'home.html', context)