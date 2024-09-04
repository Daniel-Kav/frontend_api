from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Task
from .forms import TaskForm,RegistrationForm

# Create your views here.
@login_required
def TaskList(request):
    tasks = Task.objects.filter(user = request.user)
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'form': form})

@login_required
def TaskUpdate(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_update.html', {'form': form})

@login_required
def TaskDelete(request, pk):
    task = get_object_or_404(Task, id=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_delete_confirm.html', {'task': task})

def Register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task_list')
        else:
            form = RegistrationForm()
        return render(request, 'tasks/register.html', {'form': form})