from django.shortcuts import render

# Create your views here.
def homeView(request):
    return render(request, 'todos/home.html')
