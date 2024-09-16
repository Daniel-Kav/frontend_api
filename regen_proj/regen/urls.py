from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns =[
    path('', views.dashboard, name='dashboard'),
    path('add-income', views.add_income, name='add_income'),
    path('add-expense', views.add_expenses, name='add_expense'),
    path('login', LoginView.as_view(template_name = 'regen/login'), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('edit-income/<int:pk>', views.edit_income, name='edit_income'),
    path('edit-income/<int:pk>', views.edit_income, name='edit_expense'),
    path('del-income/<int:pk>',views.del_income, name='del_income'),
    path('del-expenses/<int:pk>',views.del_expenses, name='del_expense'),
]