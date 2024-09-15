from django.shortcuts import render,redirect,get_object_or_404
from .forms import ExpenseForm,IncomeForm
from .models import Expense,Category,Income
from django.contrib.auth.decorators import login_required


# Create your views here.
def dashboard(request):
    incomes = Income.objects.filter(user = request.user)
    expenses = Expense.objects.filter(user = request.user)
    total_expenses = sum(expense.amount for expense in expenses)
    total_income = sum(income.amount for income in incomes)
    balance = total_income - total_expenses
    context = {
        'incomes': incomes,
        'balance': balance,
        'expenses': expenses,
        'total_expenses': total_expenses,
        'total_income': total_income,
    }

    return render(request, 'tracker/darshboard.html', context)

def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save( commit= False )
            income.user = request.user
            income.save()
            return redirect('dashboard')
    else:
        form = IncomeForm()
    return render(request, 'tracker/add_income.html', {'form': form})


def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save( commit=False )
            expense.user = request.user
            expense.save()
            return redirect('dashboard')
    else:
        form = ExpenseForm()
    return render(request, 'tracker/add_expense.html',{'form': form})

def del_income(request, pk):
    income = get_object_or_404(Income, pk=pk)
    if request.method == 'POST':
        income.delete()
        return redirect('dashboard')
    return render(request,'tracker/del_income.html',{'income':income})
    
def del_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == 'POST':
        expense.delete()
        return redirect('dashboard')
    return render(request,'tracker/del_expense.html',{'expense':expense})