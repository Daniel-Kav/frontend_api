from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add-income/', views.add_income, name='add_income'),
    path('add-expense/', views.add_expense, name='add_expense'),
    path('del-income/<int:pk>', views.del_income, name='del_income'),
    path('del-expense/<int:pk>', views.del_expense, name='del_expense'),
]