from django.shortcuts import render, get_object_or_404
from  .models import Job

# Create your views here.
def home(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/home.html', {'jobs': jobs})

def job_detail(request, pk):
    job = get_object_or_404(Job , pk = pk)
    return render(request, 'jobs/detail.html', {'job': job})

