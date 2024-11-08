from django.shortcuts import render,HttpResponse

# Create your views here.
def sampleView(request):
    return HttpResponse("Helo this worked")
