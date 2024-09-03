from django.shortcuts import render
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

    return render(request, 'tasks/task_list.html',{'tasks': tasks, 'form': form })
