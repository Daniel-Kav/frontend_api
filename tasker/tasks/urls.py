from django.urls import path
from . import views

urlpatterns = [
    path('',views.task_list,name='task_list'),
    path('task/<int:pk>/',views.task_detail, name='task_detail'),
    path('task/<int:pk>/update/',views.task_update, name = 'task_update'),
    path('new-task/',views.add_task,name='new_task'),
    path('delete/<int:pk>/',views.del_task, name = 'task_delete'),
]