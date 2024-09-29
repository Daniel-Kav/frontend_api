from django.urls import path
from . import views

urlpatterns =[
    path('', views.HomeView.as_view(), name='home'),
    path('new/',views.GeeksCreate.as_view(), name='new'),
]