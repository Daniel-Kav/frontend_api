from django.shortcuts import render
from .models import Expense,Income

# Create your views here.
def dashboard(request):
    incomes = Income.objects.filter(User = request.user)
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
    pass


def add_expenses(request):
    pass