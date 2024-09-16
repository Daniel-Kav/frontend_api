from django.urls import path
from . import views
from django

urlpatterns =[
    path('', views.dashboard, name='dashboard'),
    path('add-income', views.add_income, name='add_income'),
    path('add-expense', views.add_expenses, name='add_expense'),
    path('login', views.login, name='login'),
]