from django.shortcuts import render
from .forms import PizzaForm, MultiplePizzaForm
# Create your views here.
def home(request):
    return render(request , 'pizza/home.html')

def order(request):
    multi_form = MultiplePizzaForm
    if request.method == 'POST':
        form_data = PizzaForm(request.POST)
        if form_data.is_valid():
            note = "Thanks for ordering. Your %s %s %s pizza order is enroute." % (form_data.cleaned_data['size'], form_data.cleaned_data['topping1'], form_data.cleaned_data['topping2'])
            return   render(request , 'pizza/order.html', {'orderform':PizzaForm(), "note" : note, "multi_form" :multi_form})
    else:
        return   render(request , 'pizza/order.html', {'orderform':PizzaForm(), 'multi_form':multi_form})