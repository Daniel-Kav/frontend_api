from django.shortcuts import render,redirect
from .models import Sample
from .forms import SampleForm

# Create your views here.
def home_view(request):
    samples = Sample.objects.all()
    return render(request, 'samples/home.html',{"samples":samples})

def new_sample_view(request):
    if request.method == 'POST':
        form = SampleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SampleForm()
    return render(request, 'samples/new_sample.html', {'form': form})



