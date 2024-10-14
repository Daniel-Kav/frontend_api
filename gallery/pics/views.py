from django.shortcuts import render,redirect
from .models import Product
from .forms import ProductForm

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, 'pics/index.html',{'products': products})

def add_product(request):
    form = ProductForm
    if request.method == 'POST':
        form = ProductForm(request.data)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request,'pics/pform.html',{'form': form})