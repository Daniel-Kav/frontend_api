from django.urls import path
from . import views



urlpatterns = [
    path('', views.TaskList, name='task_list'),
    path('edit/<int:pk>', views.TaskUpdate, name='task_update'),
]