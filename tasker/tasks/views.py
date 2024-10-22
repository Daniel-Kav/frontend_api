from django.shortcuts import render,get_object_or_404,redirect
from .models import Task
from .forms  import TaskForm

# Create your views here.
def task_list(request):
    tasks = Task.objects.all()
    return render(request,'tasks.html',{'tasks': tasks})

def add_task(request):
    task = TaskForm(request.POST)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request,'newTask.html',{'form' : form})

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)

    return render(request, 'detail.html',{'task': task})

def task_update(request,pk):
    task = get_object_or_404(Task, pk = pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request,'update.html',{'task':task,'form': form})

def del_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'delete.html')