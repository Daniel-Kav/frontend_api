from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add-income/', views.add_income, name='add_income'),
    path('add-expense/', views.add_expense, name='add_expense'),
    path('del-income/<int:pk>', views.del_income, name='del_income'),
    path('del-expense/<int:pk>', views.del_expense, name='del_expense'),
    path('edit-expense/<int:pk>', views.edit_expense, name='edit_expense'),
    path('edit-income/<int:pk>', views.edit_income, name='edit_income'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='tracker/login.html'), name='login'),
    path('login/', LogoutView.as_view(), name='logout'),
]