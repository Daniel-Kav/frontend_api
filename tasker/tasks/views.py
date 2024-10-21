from django.shortcuts import render,get_object_or_404
from .models import Task

# Create your views here.
def task_list(request):
    tasks = Task.objects.all()
    return render(request,'tasks.html',{'tasks': tasks})

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)

    return render(request, 'detail.html',{'task': task})

def task_update(request,pk):
    task = get_object_or_404(Task, pk = pk)
    if request.method == 'POST':
        