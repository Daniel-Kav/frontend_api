
from django import forms
from .models import Category,Income,Expense


class ExpenseForm(forms.ModelForm):
    class Meta:
        model= Expense
        fields= ['category', 'description', 'amount']

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['amount', 'description']
        