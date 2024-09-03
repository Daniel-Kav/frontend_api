from django.shortcuts import render
from .forms import PizzaForm, MultiplePizzaForm
from django.forms import formset_factory
from .models import Pizza
# Create your views here.
def home(request):
    return render(request , 'pizza/home.html')

def order(request):
    multi_form = MultiplePizzaForm()
    if request.method == 'POST':
        form_data = PizzaForm(request.POST)
        created_pizza = form_data.save()
        created_pizza_pk = created_pizza.id
        if form_data.is_valid():
            note = "Thanks for ordering. Your %s %s %s pizza order is enroute." % (form_data.cleaned_data['size'], form_data.cleaned_data['topping1'], form_data.cleaned_data['topping2'])
            return   render(request , 'pizza/order.html', {'orderform':PizzaForm(), "note" : note, "multi_form" :multi_form, 'created_pizza_pk':created_pizza_pk})
    else:
        return   render(request , 'pizza/order.html', {'orderform':PizzaForm(), 'multi_form':multi_form})
    

def pizzas(request):
    number_of_pizzas = 2
    filled_multi_form = MultiplePizzaForm(request.GET)
    if filled_multi_form.is_valid():
        number_of_pizzas = filled_multi_form.cleaned_data['number']
    PizzaFormSet = formset_factory(PizzaForm, extra = number_of_pizzas)
    formset = PizzaFormSet()
    if request.method == 'POST':
        filled_formset = PizzaFormSet(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                print(form.cleaned_data['topping1'])
            note = 'Pizzas have been ordered!'
        else:
            note = 'Pizzas have not been Created!'
        return render(request, 'pizza/pizzas.html',{'note':note, 'formset':formset})
    else:
        return render(request, 'pizza/pizzas.html',{'formset':formset})


def edit_order(request, pk):
    pizza = Pizza.objects.get(pk=pk)
    form = PizzaForm(instance=pizza)
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST, instance= pizza)
        if filled_form.is_valid():
            filled_form.save()
            form = filled_form
            note = 'Your Order was successfull Updated'
        return render(request, 'pizza/edit_order.html', {'pizzaform': form, 'pizza': pizza, 'note': note})
    return render(request, 'pizza/edit_order.html', {'pizzaform': form, 'pizza': pizza})

