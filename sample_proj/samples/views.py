from django.shortcuts import render,redirect,get_object_or_404
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

def edit_sample(request, pk):
    sample = get_object_or_404(Sample, pk=pk) 
    if request.method =='POST':
        form = SampleForm(request.POST, instance=sample)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SampleForm(instance=sample)
    return render(request,'samples/edit_sample.html',{'form':form, 'sample':sample})

def delete_sample(request, pk):
    sample = get_object_or_404(Sample,pk=pk)
    if request.method == 'POST':
        sample.delete()
        return redirect('/')
    return render(request, 'samples/home.html',{'sample':sample})

