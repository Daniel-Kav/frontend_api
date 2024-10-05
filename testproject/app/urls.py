from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name= 'home'),
    path('new/', views.create_post,name= "new-post" ),
    path('new/<int:pk>/', views.post_detail, name = "post_detail"),
]