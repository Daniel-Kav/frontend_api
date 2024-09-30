from django.urls import path
from . import views

urlpatterns =[
    path('', views.HomeView.as_view(), name='home'),
    path('new/',views.GeeksCreate.as_view(), name='new'),
    path('list', views.GeeksList.as_view(), name='list'),
    path('<pk>/', views.GeeksDetail.as_view(), name='detail'),
]