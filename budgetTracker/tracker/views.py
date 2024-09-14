from django.shortcuts import render,redirect
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
        'incomes': incomes,
        'total_expenses': total_expenses,
        'total_income': total_income,
    }

    return render(request, 'tracker/dashboard.html')

def add_income(request):
    pass

def add_expense(request):
    pass
    