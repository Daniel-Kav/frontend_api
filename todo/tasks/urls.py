from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tasks',views.TaskView,'task')


urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('add-task/', views.add_task, name='add_task'),
    path('edit-task/<int:pk>', views.edit_task, name='edit_task'),
    path('del-task/<int:pk>', views.del_task, name='del_task'),
    path('', include(router.urls))
]