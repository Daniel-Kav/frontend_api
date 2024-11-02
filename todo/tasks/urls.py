from django.urls import path
from . import views


urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('add-task/', views.add_task, name='add_task'),
    path('edit-task/<int:pk>', views.edit_task, name='edit_task'),
]