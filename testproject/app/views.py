from django.shortcuts import render,redirect
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

# @login_required
# def create_post(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit= False)
#             post.user = request.user
#             post.save()
#             return redirect("home")
#     else:
#         form = PostForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'post.html', context)

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # Don't save yet
            post.author = request.user  # Set the author
            post.save()  # Now save the post
            return redirect('home')  # Redirect to a success page or home
    else:
        form = PostForm()
    return render(request, 'post.html', {'form': form})

def post_detail(request, pk):
    pass