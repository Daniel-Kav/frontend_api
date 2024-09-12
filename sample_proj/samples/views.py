from django.shortcuts import render,redirect
from .models import Sample
from .forms import SampleForm

# Create your views here.
def home_view(request):
    samples = Sample.objects.all()

    if request.method == 'POST':
        form = SampleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')



    return render(request, 'samples/home.html',{"samples":samples, "form":form})


