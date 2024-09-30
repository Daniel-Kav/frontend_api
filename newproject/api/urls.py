from django.urls import path
from . import views

urlpatterns = [
    path('users/',views.get_user, name='users' ),
    path('users/create/', views.create_user, name='create_user' ),
]