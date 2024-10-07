from django import path
from . import views


urlpatterns = [
    path('',views.TodoView.as_view(), name= 'todo_list')
]