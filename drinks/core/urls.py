from django.urls import path
from . import views


urlpatterns = [
    path('drinks/', views.drink_list, name='drink_list'),
    path('drinks/<int:pk>', views.drink_detail, name='drink_detail'),
]