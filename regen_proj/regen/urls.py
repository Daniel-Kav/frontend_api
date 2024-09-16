from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns =[
    path('', views.dashboard, name='dashboard'),
    path('add-income', views.add_income, name='add_income'),
    path('add-expense', views.add_expenses, name='add_expense'),
    path('login', LoginView.as_view(template_name = 'regen/login'), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
]