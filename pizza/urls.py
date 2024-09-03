from . import views
from django.urls import path


urlpatterns = [
    path('',views.home, name='home'),
    path('order',views.order, name='order'),
    path('pizzas',views.pizzas, name='pizzas'),
]