from django.shortcuts import render

# Create your views here.

def home (request):
    if request.method == 'POST':
        text = request.POST['text']

        if text != '':
            word = len(text.split())
            i = True
            return render(request, 'counter/home.html',
                           {'word': word, 
                            'text': text,
                            'on': 'active'})
        else:
            return render(request, 'counter/home.html',  {'on': 'active'})
    else:
        return render(request, 'counter/home.html', {'on': 'active'})

def counter(request):
    if request.method == 'POST':
        text = request.POST['text']

        if text != '':
            word = len(text.split())
            i = True
            return render(request, 'counter/home.html',
                           {'word': word, 
                            'text': text,
                            'on': 'active'})
        else:
            return render(request, 'counter/home.html',  {'on': 'active'})
    else:
        return render(request, 'counter/home.html', {'on': 'active'})