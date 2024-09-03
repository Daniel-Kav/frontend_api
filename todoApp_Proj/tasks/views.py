from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm

# Create your views here.
def TaskList(request):
    tasks = Task.objects.all()
    form  = TaskForm()
    if  request.method == 'POST':
        if form.is_valid():
            form =  TaskForm(request.POST)
            form.save()
            return redirect('task_list')

    return render(request, 'tasks/task_list.html',{'tasks': tasks, 'form': form })
