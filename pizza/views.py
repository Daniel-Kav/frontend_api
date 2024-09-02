from django.shortcuts import render
from .forms import PizzaForm
# Create your views here.
def home(request):
    return render(request , 'pizza/home.html')

def order(request):
    if request.method == 'POST':
        form_data = PizzaForm(request.POST)
        if form_data.is_valid():
            note = "Thanks for your %s %s %s pizza order is enroute." % (form_data.cleaned_data['sizes'], form_data.cleaned_data['topping1'], form_data.cleaned_data['topping2'])
            return   render(request , 'pizza/order.html', {'orderform':PizzaForm(), "note" : note})
        return   render(request , 'pizza/order.html', {'orderform':PizzaForm()})
    else:
        return   render(request , 'pizza/order.html', {'orderform':PizzaForm()})