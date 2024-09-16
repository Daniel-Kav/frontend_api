from django.shortcuts import render,redirect
from .models import Expense,Income
from .forms import IncomeForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def dashboard(request):
    incomes = Income.objects.filter(user = request.user)
    expenses = Expense.objects.filter(user = request.user)
    total_income =sum(income.amount for income in incomes)
    total_expenses = sum(expense.amount for expense in expenses)
    balance = total_income - total_expenses

    context = {
        'incomes': incomes,
        'expenses':expenses,
        'balance':balance,
        'total_income':total_income,
        'total_expenses':total_expenses
    }
    return render(request, 'regen/darshboard.html', context)

def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user
            income.save()
            return redirect('dashboard')
    else:
        form = IncomeForm()
    return render(request, 'regen/add_income.html', {'form': form})


def add_expenses(request):
    pass

def edit_income(request, pk ):
    pass

def edit_expenses(request, pk):
    pass

def del_income(request, pk):
    pass
def del_expenses(request, pk):
    pass