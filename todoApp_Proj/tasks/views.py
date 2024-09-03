from django.shortcuts import render

# Create your views here.
def TaskList(request):
    return render(request, 'task_list.html',{}   )
