from django.urls import path
from . import views



urlpatterns = [
    path('', views.TaskList, name='task_list'),
    path('edit/<int:pk>', views.TaskUpdate, name='task_update'),
    path('delete/<int:pk>', views.TaskDelete, name='task_delete'),
    path('register', views.Register, name='register')

]